from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('id', 'train_name', 'time_created', 'time_update', 'author')
    list_display_links = ('id', 'train_name')
    search_fields = ('train_name',)
    list_filter = ('time_created',)
    prepopulated_fields = {'slug': ('train_name',)}


class MusclesAdmin(admin.ModelAdmin):
    list_display = ('id', 'muscles_name')
    list_display_links = ('id', 'muscles_name')
    search_fields = ('muscles_name',)


class ProfileAdmin(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Профиль'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileAdmin,)

admin.site.register(Training, TrainingAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Muscles, MusclesAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)