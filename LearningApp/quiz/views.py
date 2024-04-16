from django.shortcuts import render
from .models import Categories, Subject
from django.http import Http404

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


def about(request):

    return render(request, "quiz/about.html")


def categories(request, subject: str):
    if Subject.objects.filter(name__iexact=subject).exists():
        context = {
            'categories': Categories.objects.filter(subject__name__iexact=subject),  # iexact um upper-lower-case zu ignorieren
            'subject': subject
        }

        return render(request, "quiz/quizzing.html", context)

    else:
        raise Http404('Ooops! Diese Seite existiert leider nicht.')