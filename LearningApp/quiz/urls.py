from django.urls import path
from . import views


urlpatterns = [
    path("", views.quiz, name="home"),
    path("account", views.account, name="account"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registration", views.registration, name="registration"),
]
