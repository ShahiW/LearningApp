from django.shortcuts import render
from .models import Category, Subject, Question, Answer, Score
from django.http import Http404
from django.contrib import messages


def home(request):
    return render(request, "quiz/base.html")


def about(request):
    return render(request, "quiz/about.html")


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