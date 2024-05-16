from django.contrib import admin
from .models import Subject, Category, Question, Answer, Classroom, Score


# Register your models here
admin.site.register(Score)


# CLASSROOM
@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = (
        "class_number",
        "class_character",
    )


# QUESTION
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "question",
        "marks",
    )

    list_filter = ["category"]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            for field in ["category", "id"]:
                form.base_fields[field].disabled = True
        return form


# ANSWER
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "answer",
        "is_correct",
    )

    list_filter = ["is_correct", "question__category__grade"]


# SUBJECT
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )


#CATEGORY
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "subject",
        "grade",
    )

    list_filter= ["grade", "subject"]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields["id"].disabled = True
        return form
    





