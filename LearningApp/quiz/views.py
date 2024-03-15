from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods


# Create your views here.

def home(request):
    return render(request, "quiz/base.html")


@require_http_methods(["GET", "POST"])
def account(request):
    return render(request, "quiz/account.html")


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == "POST":  # wurden Daten hierhin geschickt?
        benutzername = request.POST["username"]
        passwort = request.POST["password"]

        # sind die Daten valide?
        benutzer = authenticate(request, username=benutzername, password=passwort)

        if benutzer is not None:
            login(request, benutzer)
            # nach erfolgreichem login, soll nutzer auf eine seite weitergeleitet werden: from django.shortcuts import redirect
            return redirect("quiz")
        else:
            messages.error(request, "Benutzername oder Passwort nicht korrekt.")

    return render(request, "quiz/login.html")


def logout_view(request):
    logout(request)
    return redirect("quiz")


@require_http_methods(["GET", "POST"])
def registration(request):
    if request.method == "POST":  # wurden Daten hierhin geschickt?
        benutzername = request.POST["username"]
        vorname = request.POST["first"]
        nachname = request.POST["last"]
        email = request.POST["email"]
        passwort = request.POST["password"]

        user = User.objects.create_user(benutzername, email, passwort, first_name=vorname, last_name=nachname)

        login(request, user)

        return redirect("quiz")

    else:
        return render(request, "quiz/registration.html")
    
