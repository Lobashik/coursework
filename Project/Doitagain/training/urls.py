from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('training/<int:trainid>/', training),
    path('about/', about),
    path('exercises/', exercises),
]