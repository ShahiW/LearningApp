from django.shortcuts import render
from .models import Categories, QuestionAnswer

#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
#from django.views.decorators.http import require_http_methods


# Beispiel:
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }

#     return render(request, "quiz/base.html", context)


def home(request):
    return render(request, 'quiz/base.html')


def deutsch(request):
    context = {"categoriess": Categories.objects.filter(subject__name="Deutsch")}
    return render(request, "quiz/deutsch.html", context)


def mathe(request):
    context = {"categoriess": Categories.objects.filter(subject__name='Mathe')}

    return render(request, "quiz/mathe.html", context)


def about(request):

    return render(request, "quiz/about.html")


def quizzing(request):
    context = {'questions': QuestionAnswer.objects.all()}
    
    return render(request, "quiz/quizzing.html", context)