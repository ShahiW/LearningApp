# Generated by Django 4.2.13 on 2024-05-28 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_alter_score_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='quiz.subject'),
        ),
    ]
