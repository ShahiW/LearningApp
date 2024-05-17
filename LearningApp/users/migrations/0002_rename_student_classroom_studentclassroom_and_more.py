# Generated by Django 5.0.3 on 2024-05-16 07:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_delete_grade'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student_Classroom',
            new_name='StudentClassroom',
        ),
        migrations.RenameModel(
            old_name='Subject_Teacher',
            new_name='SubjectTeacher',
        ),
        migrations.RenameModel(
            old_name='Teacher_Classroom',
            new_name='TeacherClassroom',
        ),
    ]