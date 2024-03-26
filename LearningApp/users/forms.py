from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Meine Models
class UserRegisterForm(UserCreationForm):  # Diese Form erbt von der User creation form
    email = forms.EmailField()  # default: required=True, sollte Email optional, dann auf False setzten

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Reihenfolge in der Liste ist Reihenfolge im Frontend


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']