from django.contrib import admin
from .models import Subject, Category, Question, Answer, Classroom, Score

# Register your models here.
admin.site.register(Subject)
admin.site.register(Answer)
admin.site.register(Classroom)
admin.site.register(Score)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "question",
        "marks",
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            for field in ["category", "id"]:
                form.base_fields[field].disabled = True
        return form
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields["id"].disabled = True
        return form