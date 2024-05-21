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
    image = models.ImageField(default='avatar1.png', upload_to='profile_pics') 


    # neue Idee für random Bilder aus einer Liste:
    # image_list = []
    # for filename in glob.glob("*.png"):
    #     im = Image.open(filename)
    #     image_list.append(im)

    #     for img in image_list: 
    #         choice = random.randint(0, len(image_list) - 1)
    #         random_image = image_list[
    #             choice
    #         ]  

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
    
