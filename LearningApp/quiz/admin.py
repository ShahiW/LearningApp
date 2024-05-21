from django.contrib import admin
from .models import Subject, Category, Question, Answer, Classroom, Score

from django_admin_listfilter_dropdown.filters import (
    DropdownFilter,
    ChoiceDropdownFilter,
    RelatedDropdownFilter,
)


class EntityAdmin(admin.ModelAdmin):
    list_filter = (
        # for ordinary fields
        ("a_charfield", DropdownFilter),
        # for choice fields
        ("a_choicefield", ChoiceDropdownFilter),
        # for related fields
        ("a_foreignkey_field", RelatedDropdownFilter),
    )


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

    list_filter = ["category", "category__subject"]

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
        #"is_correct",
    )

    list_filter = ["is_correct", "question__category__subject", "question__category"]


# SUBJECT
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "class_number",
    )


#CATEGORY
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "subject",
        #"grade",
    )

    list_filter= ["subject"]  # "grade",

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields["id"].disabled = True
        return form
    


