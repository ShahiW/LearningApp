from django.db import models
from django.contrib.auth.models import User  
# from django.contrib.auth.models import AbstractUser
from PIL import Image  # aus Pillow Lib importiere die Klasse Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # for profile picture
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profil'
    
    def save(self, *args, **kwargs):
        # Speichere die Bilddatei. Das wäre eh passiert. Aber es soll noch eine Funktionalität ergänzt werden.
        super(Profile, self).save(*args, **kwargs)  
        
        # Öffne die Bilddatei
        image = Image.open(self.image.path) 
        # Checke Bilddateityp
        if image.mode in ('JPG'):
        # Konvertiere Image von JPG zu PNG
            image = image.convert('RGB')

    
        # Check ob Bildgröße der Bedingung enspricht:
        if image.height > 100 or image.width > 100:
            # Tuple der Max-Größe, kann in Zukunft einfach angepasst werden
            output_size = (300, 300)
            # Mache dieses Bild zu einem Thumbnail
            image.thumbnail(output_size)
            # Überschreibe die Bilddatei mit dem Thumbnail
            image.save(self.image.path)

"""
1.) import ist noch auskommentiert!!!
2.) in forms.py in users: user_permissions auskommentiert
3.) Wenn das hier richtig ist, dann muss noch AUTH_USER_MODEL = 'User_Role' in settings.py hinzugefügt werden mit
Hinweis: UPDATE: To create relation to custom user model:
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
source: https://stackoverflow.com/questions/29691116/django-1-7-add-or-change-a-related-name-argument-to-the-definition-for

class User_Role(AbstractUser):
    ROLE_CHOICES = (
        ("administrator", "Administrator"),
        ("teacher", "Teacher"),
        ("student", "Student"),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_class = models.CharField(max_length=3)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    school_class = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
"""