from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.show_questions, name="about"),
    path("categories/<str:subject>", views.categories, name="categories"),
    path("quiz/<uuid:c_id>", views.quiz, name="quiz"),
    path("check_answer/<uuid:a_id>", views.check_answer, name="check_answer"),
]