# Generated by Django 5.0.3 on 2024-05-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_delete_grade'),
        ('users', '0002_rename_student_classroom_studentclassroom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectteacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='subjectteacher',
            name='subject',
            field=models.ManyToManyField(to='quiz.subject'),
        ),
    ]