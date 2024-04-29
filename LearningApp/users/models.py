from django.db import models
from django.contrib.auth.models import User  
# from django.contrib.auth.models import AbstractUser
from PIL import Image  # aus Pillow Lib importiere die Klasse Image
from quiz.models import Subject, Classroom


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
1.) https://docs.djangoproject.com/en/dev/topics/auth/default/#permissions-and-authorization
2.) https://docs.djangoproject.com/en/dev/ref/contrib/auth/#django.contrib.auth.models.User
3.) Auf Admin page permissions der jeweiligen Gruppe erteilen.
"""

# Tabelle Lehrer
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name
    

# Tabelle Schüler
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"