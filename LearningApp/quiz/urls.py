from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("categories/<str:subject>", views.categories, name="categories"),
    path("quiz/<uuid:id>", views.quiz, name="quiz"),
]