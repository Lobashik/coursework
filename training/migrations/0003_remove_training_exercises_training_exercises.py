# Generated by Django 4.1.5 on 2023-05-07 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("training", "0002_remove_training_exercises_training_exercises"),
    ]

    operations = [
        migrations.RemoveField(model_name="training", name="exercises",),
        migrations.AddField(
            model_name="training",
            name="exercises",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="training.exercise",
                verbose_name="Упражнения",
            ),
        ),
    ]
