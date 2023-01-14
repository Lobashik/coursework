from django.db import models

class Exercises(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    muscles = models.CharField(max_length=64)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.title


# class Training(models.Models):
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     time_created = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     author = models.


# class Users(models.Model):
#     name = models.CharField(max_length=64)
#     age = models.SmallIntegerField()
#     trainings = models.
#     like_exercises = models.TextField()