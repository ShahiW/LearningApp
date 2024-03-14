from django.db import models
from django.contrib.auth.models import User

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
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    

