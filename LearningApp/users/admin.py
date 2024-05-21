from django.contrib import admin
from .models import (
    Profile,
    StudentClassroom,
    TeacherClassroom,
    SubjectTeacher,
    StudentQuizScore,
)

admin.site.register(Profile)

@admin.register(StudentClassroom)
class StudentClassroomAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "classroom",
    )

    # def get_form(self, request, obj=None, **kwargs):
    # form = super().get_form(request, obj, **kwargs)
    # is_superuser = request.user.is_superuser

    # if not is_superuser:
    #     for field in ["category", "id"]:
    #         form.base_fields[field].disabled = True
    # return form


@admin.register(SubjectTeacher)
class SubjectTeacherAdmin(admin.ModelAdmin):
    list_display = (
        "teacher",
    )


@admin.register(TeacherClassroom)
class TeacherClassroomAdmin(admin.ModelAdmin):
    list_display = (
        "teacher",
        )
    

@admin.register(StudentQuizScore)
class StudentQuizScoreAdmin(admin.ModelAdmin):
    list_display = (
        "user", 
        "subject",
        "category",
        "value",
    )