from django.shortcuts import render
from .models import Category, Subject, Question, Answer, Score
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection  # zeigt queries genauer und wie schnell performed
from django.db.models import Q  # Keyword argument queries


def home(request):
    return render(request, "quiz/base.html")


def about(request):
    return render(request, "quiz/about.html")


@login_required
def categories(request, subject: str):
    if Subject.objects.filter(name__iexact=subject).exists():
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
def quiz(request, c_id):
    # if question.is_answered:
    # question = Question.objects.filter(category__id=c_id).except(is_answered=True).first()
    user = request.user
    question = Question.objects.filter(category__id=c_id).first()
    if question:
        context = {
            "category": Category.objects.get(id=c_id),
            "question": question,
            "answers": Answer.objects.filter(question__id=question.id),
        }

        return render(request, "quiz/quiz.html", context)
    else:
        raise Http404("Ooops! Diese Frage existiert leider nicht.")

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

# ORM Tutorial

# OR QUERIES
##########################################
#def show_questions_(request):
    #questions = Question.objects.all()

    #print(questions)
    #print(questions.query)
    #print(connection.queries)

    #return render(request, "quiz/about.html", {'questions': questions})

# OR Query
#def show_questions_(request):
        #questions = Question.objects.filter(marks=1) | Question.objects.filter(question__startswith=48)

        #print(questions)
        #print(connection.queries)

        #return render(request, "quiz/about.html", {"questions": questions})

# Q objects: 
def show_questions(request):
    questions = Question.objects.filter(Q(marks=1) 
                                        | Q(question__startswith=48) 
                                        | ~Q(marks=2))  # not mark

    print(questions)
    print(connection.queries)

    return render(request, "quiz/about.html", {"questions": questions})

    
# AND QUERIES
##########################################