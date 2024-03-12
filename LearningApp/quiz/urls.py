from django.urls import path
from . import views



urlpatterns = [
    path("", views.quiz, name="quiz"),
    path("login", views.loginSeite, name="login"),
    path("registration", views.registration, name="registration"),
]
