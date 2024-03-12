# User registrieren und anmelden

Hilfreiche Seiten:

1. [Django Docs User objects](https://docs.djangoproject.com/en/5.0/topics/auth/default/#topics-auth-creating-users)
1. [Erlaubte HTTP Methoden](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#allowed-http-methods)

## Creating users

Der einfachste Weg, um Benutzer zu erstellen, ist die Verwendung der integrierten Hilfsfunktion __create_user()__:

```python
from django.contrib.auth.models import User
user = User.objects.create_user("john", "<lennon@thebeatles.com>", "johnpassword")

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields

user.last_name = "Lennon"
user.save()
```

## Decorater über jede Views Funktion

```python
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass
```

## Beispiel: Meine Anwendung (LearningApp)

Registrierung:

```python
@require_http_methods(["GET", "POST"])
def registration(request):
    if request.method == "POST":  # wurden Daten hierhin geschickt?
        benutzername = request.POST("username")
        vorname = request.POST("first")
        nachname = request.POST("last")
        email = request.POST("email")
        passwort = request.POST("password")

        user = User.objects.create_user(benutzername, email, passwort, first_name=vorname, last_name=nachname)

        login(request, user)

        return redirect("quiz")

    else:
        return render(request, "quiz/registration.html")
```

Login:

```python
@require_http_methods(["GET", "POST"])
def loginSeite(request):
    if request.method == "POST":  # wurden Daten hierhin geschickt?
        benutzername = request.POST("username")
        passwort = request.POST("password")

        # sind die Daten valide?
        benutzer = authenticate(request, username=benutzername, password=passwort)

        if benutzer is not None:
            login(request, benutzer)
            # nach erfolgreichem login, soll nutzer auf eine seite weitergeleitet werden: from django.shortcuts import redirect
            return redirect("quiz")
        else:
            messages.error(request, "Benutzername oder Passwort nicht korrekt.")

    return render(request, "quiz/login.html")
```

## In den Templates: (registration.html + login.html)

```python
<form method="POST">
        ...
</form>
```
