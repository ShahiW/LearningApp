from django.shortcuts import render
from .models import Category, Subject
from django.http import Http404





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

        return render(request, "quiz/quizzing.html", context)

    else:
        raise Http404("Ooops! Diese Seite existiert leider nicht.")