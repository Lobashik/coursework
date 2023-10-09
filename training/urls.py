from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', DoItAgain.as_view(), name='home'),
    path('trains/', Trains.as_view(), name='trains'),
    path('trains/<slug:training_slug>/', ShowTrain.as_view(), name='train'),
    path('add_train/', AddTrain.as_view(), name='add_train'),
    path('about/', about, name='about'),
    path('exercises/', Exercises.as_view(), name='exercises'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:pk>/', ShowProfile.as_view(), name='profiles'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('exercises/<slug:exercise_slug>/', ShowExercise.as_view(), name='show_exercises'),
]