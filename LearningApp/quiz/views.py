from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Category, Subject, Question
from django.http import Http404
import random


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
    

def quiz(request, id):
    context = {
        'category': Category.objects.get(id=id),
        'questions': Question.objects.filter(category__id=id),
        }
    return render(request, 'quiz/quiz.html', context)



def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        if request.GET.get("category"):
            question_objs = question_objs.filter(
                category__name__icontains=request.GET.get("category")
            )

        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append(
                {
                    "uid": question_obj.id,
                    "category": question_obj.category.name,
                    "question": question_obj.question,
                    "marks": question_obj.marks,
                    "answer": question_obj.get_answers(),
                }
            )

        payload = {"status": True, "data": data}

        return JsonResponse(payload)  # Return JsonResponse

    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")
