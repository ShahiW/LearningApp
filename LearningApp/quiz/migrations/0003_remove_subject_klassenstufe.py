# Generated by Django 5.0.3 on 2024-05-15 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_category_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='klassenstufe',
        ),
    ]
