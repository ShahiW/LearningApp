from django.shortcuts import render
from .models import Category, Subject, Question, Answer, Score
from users.models import StudentClassroom, StudentQuizScore
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from uuid import UUID
from django.db.models import Sum
from random import choice


def home(request):
    return render(request, "quiz/base.html")


def about(request):
    return render(request, "quiz/about.html")


@login_required
def subjects(request):
    user = request.user
    classrooms = StudentClassroom.objects.filter(student=user)

    if classrooms: 
        student_year = classrooms[0].classroom.class_number
        context = {"subjects": Subject.objects.filter(class_number=student_year)}

    else:
        context = {"subjects": Subject.objects.all()}

    return render(request, "quiz/categories.html", context)


@login_required
def categories(request, subject: str, class_number: int):
    if Subject.objects.filter(name__iexact=subject, class_number=class_number).exists():

        context = {
            "categories": Category.objects.filter(
                subject__name__iexact=subject, subject__class_number=class_number
            ),  # iexact um upper-lower-case zu ignorieren
            "subject": subject,
            "class_number": class_number,
        }

        return render(request, "quiz/category.html", context)

    else:
        raise Http404("Ooops! Diese Seite existiert leider nicht.")


@login_required
def quiz(request, c_id: UUID):
    user = request.user
    # Gesamtpunktzahl für Quiz
    total_score = Question.objects.filter(category__id=c_id).aggregate(Sum("marks", default=0))["marks__sum"]

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
        quiz_score = Score.objects.filter(category__id=c_id, user=user).aggregate(Sum("value", default=0))["value__sum"]

        context = {
            "score": quiz_score,
            "total_score": total_score,
        }

        response = render(request, "quiz/quiz-finished.html", context)
        
        # quiz score in studentquizscore speichern
        subject = Subject.objects.get(category__id=c_id)#
        category = Category.objects.get(id=c_id)
        StudentQuizScore.objects.update_or_create(user=user, subject=subject, category=category, defaults={"value": quiz_score})
        # score zurücksetzen
        Score.objects.filter(category__id=c_id, user=user).update(value=None)
        return response


@login_required
def check_answer(request, a_id):
    answer = Answer.objects.get(id=a_id)
    question = answer.question
    right_answer = Answer.objects.get(is_correct=True, question=question)
    category = question.category
    subject = category.subject
    user = request.user

    if answer.is_correct:
        score = question.marks
    else:
        score = 0
        messages.info(request, f'Leider falsch. Die richtige Antwort war "{ right_answer }".')

    Score.objects.update_or_create(
        user=user,
        subject=subject,
        category=category,
        question = question,
        defaults={"value": score},
    )

    return quiz(request, category.id)


@login_required
def user_page(request):
    user = request.user
    if user.is_staff:
        return render(request, "quiz/base.html")

    else:
        classrooms = StudentClassroom.objects.filter(student=request.user)
        student_class = classrooms[0].classroom.class_number
        quizzes_done = StudentQuizScore.objects.filter(user=request.user)
        quizzes_left_ids = (
            Category.objects.filter(subject__class_number=student_class)
            .exclude(id__in=[c.category.id for c in quizzes_done])
            .values_list("id", flat=True)
        )

        if quizzes_left_ids:
            random_id = choice(quizzes_left_ids)

            context = {"random_category": Category.objects.get(id=random_id)}

        else:
            quizzes_id = Category.objects.filter(subject__class_number=student_class).values_list('id', flat=True)

            random_id = choice(quizzes_id)
            random_category = Category.objects.get(id=random_id)

            context = {"random_category": random_category}

        return render(request, "quiz/user-page.html", context)