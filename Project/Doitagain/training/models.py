from django.db import models
from django.urls import reverse

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    muscles = models.ImageField(upload_to="photos/%Y/%m/%d/")
    level = models.IntegerField() # Уровень от 1 до 10, но потом округляется до 5-х бальной шкалы
    train = models.ForeignKey('Training', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_urls(self):
        return reverse('show_exercises', kwargs={'exercises_id': self.pk})

class Training(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Users', on_delete=models.PROTECT, null=True)
    exercises = models.ForeignKey('Exercise', on_delete=models.PROTECT, related_name='name', null=True)
    muscles = models.ImageField(upload_to="photos/%Y/%m/%d")
    train_level = models.ForeignKey('Exercise', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Users(models.Model):
    user_name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    trainings = models.ForeignKey('Training', on_delete=models.PROTECT, null=True)
    like_exercises = models.TextField(blank=True)
    
    def __str__(self):
        return self.user_name