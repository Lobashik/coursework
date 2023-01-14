from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ["Главная страница", "О сайте", "Упражнения", "Тренировки", "Войти"]

def index(request):
    return render(request, 'training/index.html', {'menu': menu, 'title': 'Главная станица'})

def about(request):
    return render(request, 'training/about.html', {'menu': menu, 'title': 'О сайте'})

def exercises(request):
    exercises = Exercises.objects.all()
    return render(request, 'training/exercises.html', {'menu': menu, 'exercises': exercises, 'title': 'Упражнения'})

def training(request, trainid):
    if int(trainid) > 999:
        return redirect('home', permanent=True)
    return HttpResponse(f"Тренировки<p>{trainid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')