from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("user-page/", views.user_page, name="user-page"),
    path("classes-overview/", views.classes_overview, name="classes-overview"),
    path("classroom/<uuid:classroom_id>", views.classroom, name="classroom"),
    path(
        "categories/<str:subject>/<int:class_number>",
        views.categories,
        name="categories",
    ),
    path("quiz/<uuid:c_id>", views.quiz, name="quiz"),
    path("check_answer/<uuid:a_id>", views.check_answer, name="check_answer"),
]