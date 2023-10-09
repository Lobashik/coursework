# Generated by Django 4.1.5 on 2023-05-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("training", "0003_remove_training_exercises_training_exercises"),
    ]

    operations = [
        migrations.RemoveField(model_name="training", name="exercises",),
        migrations.AddField(
            model_name="training",
            name="exercises",
            field=models.ManyToManyField(
                to="training.exercise", verbose_name="Упражнения"
            ),
        ),
    ]
