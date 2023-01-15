from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('training/', training, name='training'),
    path('about/', about, name='about'),
    path('exercises/', exercises, name='exercises'),
    path('login/', login, name='login'),
    path('exercises/<int:exercises_id>/', show_exercises, name='show_exercises'),
]