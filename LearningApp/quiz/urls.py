from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("subjects/", views.subjects, name="subjects"),
    path("quizzing/", views.quizzing, name="quizzing"),
]