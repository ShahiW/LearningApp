from django.contrib import admin
from .models import (
    Profile,
    Student_Classroom,
    Teacher_Classroom,
    Subject_Teacher,
)

admin.site.register(Profile)
# admin.site.register(Student_Classroom)
admin.site.register(Teacher_Classroom)
admin.site.register(Subject_Teacher)

@admin.register(Student_Classroom)
class Student_ClassroomAdmin(admin.ModelAdmin):
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