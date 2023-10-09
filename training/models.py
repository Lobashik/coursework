from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Exercise(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Описание упражнения')
    muscles_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Группа мышц')
    muscles_group = models.ForeignKey('Muscles', on_delete=models.PROTECT, verbose_name='Упражнения на мышцы', null=True)
    #views паодсчет просмотров этого упражнения


    def __str__(self):
        return self.title


    def get_absolute_urls(self):
        return reverse('show_exercises', kwargs={'exercise_slug': self.slug})
    

    class Meta:
        verbose_name = 'Упражнения'
        verbose_name_plural = 'Упражнения'
        ordering = ['title']


class Muscles(models.Model):
    muscles_name = models.CharField(max_length=255, verbose_name='Название группы мышц')


    def __str__(self):
        return self.muscles_name
    

    def get_absolute_urls(self):
        return reverse('show_muscles', kwargs={'muscles_id': self.pk})
    

    class Meta:
        verbose_name = 'Мышцы'
        verbose_name_plural = 'Мышцы'
        ordering = ['muscles_name']


class Training(models.Model):
    train_name = models.CharField(max_length=255, verbose_name='Название тренировки')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержание тренировки')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Автор', editable=False)
    exercises = models.ManyToManyField('Exercise', verbose_name='Упражнения')


    def __str__(self):
        return self.train_name
    

    def get_absolute_urls(self):
        return reverse('train', kwargs={'training_slug': self.slug})
    

    class Meta:
        verbose_name = 'Тренировки'
        verbose_name_plural = 'Тренировки'
        ordering = ['time_created']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)
    weight = models.IntegerField(verbose_name='Вес', null=True)
    height = models.IntegerField(verbose_name='Рост', null=True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
