from django.shortcuts import render
from .models import Subject
from .models import Categories

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
    content = {
        'subjects': Subject.objects.all()
    }

    return render(request, 'quiz/base.html', content)


def deutsch(request):
    content = {"categorie": Categories.objects.all()}

    return render(request, "quiz/deutsch.html", content)


def mathe(request):
    content = {"subjects": Subject.objects.all()}

    return render(request, "quiz/mathe.html", content)


def about(request):
    content = {"subjects": Subject.objects.all()}

    return render(request, "quiz/about.html", content)