from django.contrib import admin
from .models import Subject, Category, Question, Answer

# Register your models here.
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)

