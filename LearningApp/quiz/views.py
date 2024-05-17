from django.shortcuts import render
from .models import Category, Subject, Question, Answer, Score
from users.models import StudentClassroom
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from uuid import UUID
from django.db.models import Sum


def home(request):
    return render(request, "quiz/base.html")


def about(request):
    return render(request, "quiz/about.html")


@login_required
def categories(request, subject: str):
    if Subject.objects.filter(name__iexact=subject).exists():
        user = request.user
        classrooms = StudentClassroom.objects.filter(student=user)  

        # Check if Student (only students are in table StudentClassroom)
        if classrooms :
            student_year = classrooms[0].classroom.class_number
        
            context = {
                "categories": Category.objects.filter(
                    subject__name__iexact=subject, subject__year=student_year
                ),  # iexact um upper-lower-case zu ignorieren
                "subject": subject,
            }

        else:
            context = {
                "categories": Category.objects.filter(
                    subject__name__iexact=subject
                ),  # iexact um upper-lower-case zu ignorieren
                "subject": subject,
            }

        return render(request, "quiz/category.html", context)

    else:
        raise Http404("Ooops! Diese Seite existiert leider nicht.")


@login_required
def quiz(request, c_id: UUID):
    user = request.user

    questions = Question.objects.raw("""select quiz_question.id, quiz_question.question 
                                    from quiz_question left join quiz_score on quiz_question.id = quiz_score.question_id 
                                    where quiz_score.value is null and quiz_question.category_id = %s 
                                    limit 1""", [c_id.hex])  
    if questions:
        question = questions[0]
        context = {
            "category": Category.objects.get(id=c_id),
            "question": question,
            "answers": Answer.objects.filter(question=question),
        }

        return render(request, "quiz/quiz.html", context)
    
    else:
        context = {
            "score": Score.objects.filter(category__id=c_id).aggregate(Sum("value"))
        }
        return render(request, "quiz/quiz-finished.html", context)

        #raise Http404("Keine Fragen mehr!")

    # else:
    messages.info(
        request,
        f"Toll { user.username }! Du hast das Quiz beendet. Dein Punktestand ist: <score>",
    )


@login_required
def check_answer(request, a_id):
    answer = Answer.objects.get(id=a_id)
    question = answer.question
    right_answer = Answer.objects.get(is_correct=True, question=question)
    category = question.category
    subject = category.subject
    user = request.user

    if answer.is_correct:
        score = Score(
            user = user,
            subject = subject,
            category = category,
            question = question,
            value = question.marks,
        )
        score.save()
    
    else:
        messages.info(request, f"Leider falsch. Die richtige Antwort ist { right_answer }")
        score = Score(
            user = request.user,
            subject = subject,
            category = category,
            question = question,
            value = 0,
        )
        score.save()

    return quiz(request, category.id)