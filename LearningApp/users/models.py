from django.db import models
from django.contrib.auth.models import User  
from PIL import Image  # aus Pillow Lib importiere die Klasse Image
# import glob
# import os
# import random

from quiz.models import Subject, Classroom, Category

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # for profile picture
    image = models.ImageField(default='default.png', upload_to='profile_pics') 

    def __str__(self):
        return f'{self.user.username} Profil'
    
    
    def save(self, *args, **kwargs):
        # Speichere die Bilddatei. Das wäre eh passiert. Aber es soll noch eine Funktionalität ergänzt werden.
        super().save(*args, **kwargs)  
        
        # Öffne die Bilddatei
        image = Image.open(self.image.path) 

        width, height = image.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            image.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) // 2
            right = (width + height) // 2
            top = 0
            bottom = height
            image = image.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            image = image.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            image.thumbnail((300, 300))

        image.save(self.image.path)

    

# Mapping Tabelle Student-Classroom
class StudentClassroom(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} {self.classroom}"


# Mapping Tabelle Teacher-Classroom
class TeacherClassroom(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.ManyToManyField(Classroom)

    def __str__(self):
        return f"{self.teacher} {self.classroom}"


# Mapping Tabelle Subject-Teacher
class SubjectTeacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return f"{self.teacher} {self.subject}"
    

# mapping Tabelle für StudentScore
class StudentQuizScore(models.Model):
    user = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="+", on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name="+", on_delete=models.DO_NOTHING)
    value = models.IntegerField(null=False)
    
