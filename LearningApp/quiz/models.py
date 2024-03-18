from django.db import models
#from django.utils import timezone
#from django.contrib.auth.models import User

# Merke: nach jedem neuen Model makemigrations und migrate!!!

# Beispiel:
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)  # keine klammern: hier soll die Funktion noch nicht ausgeführt werden
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


# Meine Models

# Tabelle Fächer
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# Tabelle Kategorien
class Categories(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

# Tabelle Fragen und Antworten
class QuestionAnswer(models.Model):
    quiz_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()







