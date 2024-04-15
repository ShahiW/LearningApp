from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("deutsch/", views.deutsch, name="deutsch"),
    path("mathe/", views.mathe, name="mathe"),
    path("about/", views.about, name="about"),
    path("quizzing/", views.quizzing, name="quizzing"),
]