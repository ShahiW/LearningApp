# Generated by Django 5.0.3 on 2024-05-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]