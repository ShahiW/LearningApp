from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("account", views.account, name="account"),
    path("login", views.login_view, name="home"),
    path("logout", views.logout_view, name="home"),
    path("registration", views.registration, name="home"),
]
