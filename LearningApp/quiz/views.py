from django.shortcuts import render, redirect
#from .models import Post Beispiel

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



