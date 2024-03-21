# Diese Form erbt von der User creation form

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()  # default: required=True, sollte Email optional, dann auf False setzten

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']  # Reihenfolge in der Liste ist Reihenfolge im Frontend