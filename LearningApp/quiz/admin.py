from django.contrib import admin
from .models import Subject, Categories, QuestionAnswer

# Register your models here.
admin.site.register(Subject)
admin.site.register(Categories)
admin.site.register(QuestionAnswer)