from django.db.models.signals import post_save  # sobald ein Objekt gespeichert wird wird dieses Signal gesendet
from django.contrib.auth.models import User     # um post_save Signal zu bekommen, wenn ein User erzeugt wurde
from django.dispatch import receiver            # für die Empfänger-Funktion
from .models import Profile                      # in der Funktion wird ein Profil angelegt, deshalb Profile Model importieren 
from django.contrib.auth.signals import user_logged_out
from django.contrib import messages

# Das User Model wird der Sender sein
# Zusätzlich braucht man noch einen Receiver/Empfänger, hier eine Funktion, die Signal empfängt und dann was auslöst

# Wird immer ausgeführt, wenn ein User angelegt wird
@receiver(post_save, sender=User)
def create_profile(sender, instance, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # Speichert jedes neu angelegte Profil, wenn User gespeichert wird
        instance.profile.save()

# User ist der Sender, post_save ist das Signal, die Funktion create_profile ist mit dem Decorater zum Receiver geworden 
# und es wird eine Instanz von Profile mit den Userdaten erzeugt.
# Um die Funktionen nutzen zu können, müssen diese noch in der users > apps.py in die UsersConfig importiert werden.
        

# Success message nach logout
@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, "Du hast dich erfolgreich ausgeloggt")
