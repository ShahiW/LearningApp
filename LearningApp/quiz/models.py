from django.db import models
import uuid
from django.contrib.auth.models import User


# Meine Models

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


# Tabelle Fächer
class Subject(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Tabelle Kategorien
class Category(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Question(BaseModel):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question


class Answer(BaseModel):
    question = models.ForeignKey(
        Question, related_name="question_answer", on_delete=models.CASCADE
    )
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer
    

class Score(BaseModel):
    user = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="+", on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name="+", on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, related_name="+", on_delete=models.DO_NOTHING)
    value = models.IntegerField(null=False)
