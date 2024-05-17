from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    #path("subjects/", views.subjects, name="subjects"),
    path("categories/<str:subject>/<int:class_number>", views.categories, name="categories"),
    path("quiz/<uuid:c_id>", views.quiz, name="quiz"),
    path("check_answer/<uuid:a_id>", views.check_answer, name="check_answer"),
]