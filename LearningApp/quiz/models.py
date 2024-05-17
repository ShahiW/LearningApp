from django.db import models
import uuid
from django.contrib.auth.models import User


# Meine Models

# BASE MODEL, von dem geerbt wird
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


# Tabelle FÄCHER
class Subject(BaseModel):
    name = models.CharField(max_length=100)
    class_number = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.class_number}'
    

# Tabelle KLASSEN
class Classroom(BaseModel):
    class_number = models.IntegerField(default=0)
    class_character = models.CharField(max_length=10)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.class_number} {self.class_character}'


# Tabelle KATEGORIEN
class Category(BaseModel):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.name}' # ({self.grade})'
    

#Tabelle FRAGEN
class Question(BaseModel):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question


# Tabelle ANTWORTEN
class Answer(BaseModel):
    question = models.ForeignKey(
        Question, related_name="question_answer", on_delete=models.CASCADE
    )
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer
    

# Tabelle PUNKTE
class Score(BaseModel):
    user = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="+", on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name="+", on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, related_name="+", on_delete=models.DO_NOTHING)
    value = models.IntegerField(null=False)

