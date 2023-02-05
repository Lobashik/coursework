from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *


menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Упражнения", 'url_name': 'exercises'},
        {'title': "Тренировки", 'url_name': 'training'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    return render(request, 'training/index.html', {'menu': menu, 'title': 'Главная станица'})

def about(request):
    return render(request, 'training/about.html', {'menu': menu, 'title': 'О сайте'})

def exercises(request):
    exercises = Exercise.objects.all()
    context = {
        'menu': menu, 
        'exercises': exercises, 
        'title': 'Упражнения',
    }
    return render(request, 'training/exercises.html', context=context)

def training(request):
    return HttpResponse("Тренировки")

def login(request):
    return HttpResponse("Войти")

def show_exercises(request, exercises_id):
    return HttpResponse(f"Просмотр упражнения {exercises_id}")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')