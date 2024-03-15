from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

"""
class User(AbstractUser):
    LEHRER = 1
    SCHÜLER = 2

    ROLE_CHOICES = (
        (LEHRER, 'Lehrer'),
        (SCHÜLER, 'Schüler')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)



class Schüler(models.Model):
    schüler = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    vorname = models.CharField(max_length=200, null=True)
    nachname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    passwort = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.vorname
    

class Lehrer(models.Model):
    leherer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    vorname = models.CharField(max_length=200, null=True)
    nachname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    passwort = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.vorname
    

class Fach(models.Model):
    fach_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.fach_name
    

class Kategorie(models.Model):
    fach_id = models.ForeignKey(Fach, on_delete=models.CASCADE)
    kategorie_name = models.CharField(max_length=200, null=True)
"""