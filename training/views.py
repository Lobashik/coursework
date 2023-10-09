from random import randint
from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *


class DoItAgain(DataMixin, ListView):
    model = Exercise
    template_name = 'training/index.html'
    context_object_name = 'popular_exercises'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(page_title='Fitness for you')
        return dict(list(context.items()) + list(c_def.items()))


class Exercises(DataMixin, ListView):
    model = Exercise
    template_name = 'training/exercises.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(page_title='Упражнения')
        context['arms'] = Exercise.objects.filter(muscles_group=1)
        context['legs'] = Exercise.objects.filter(muscles_group=2)
        context['chest'] = Exercise.objects.filter(muscles_group=3)
        context['back'] = Exercise.objects.filter(muscles_group=4)
        context['abdominals'] = Exercise.objects.filter(muscles_group=5)
        context['exercise'] = Exercise.objects.get(id=randint(1, len(Exercise.objects.all())))
        context['muscle_group'] = Muscles.objects.order_by('muscles_name').all()
        context['title'] = 'Упражнения'
        return dict(list(context.items()) + list(c_def.items()))


class Trains(DataMixin, ListView):
    model = Training
    template_name = 'training/trains.html'
    context_object_name = 'trains'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(page_title='Тренировки')
        context['title'] = 'Тренировки'
        return dict(list(context.items()) + list(c_def.items()))


class ShowTrain(DataMixin, DetailView):
    model = Training
    template_name = 'training/train.html'
    slug_url_kwarg = 'training_slug'
    context_object_name = 'train'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(page_title=context['train'])
        context['exercises'] = context['train'].exercises
        context['title'] = 'Упражнения'
        return dict(list(context.items()) + list(c_def.items()))


class AddTrain(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTrainForm
    template_name = 'training/add_train.html'
    success_url = reverse_lazy('trains')
    #raise_exception - исключение 403 нет доступа

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(page_title='Новая тренировка')
        return dict(list(context.items()) + list(c_def.items())) 


class ShowExercise(DataMixin, DetailView):
    model = Exercise
    template_name = 'training/exercise.html'
    slug_url_kwarg = 'exercise_slug'
    context_object_name = 'exercise'

    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        c_def = self.get_user_context(page_title=context['exercise'])
        context['muscle'] = context['exercise'].muscles_group
        context['muscles_group'] = Exercise.objects.filter(muscles_group=context['exercise'].muscles_group)
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'training/register.html'
    success_url = reverse_lazy('trains')

    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        c_def = self.get_user_context(page_title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
    

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('trains')
    

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'training/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(page_title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
    

    def get_success_url(self):
        return reverse_lazy('home')
    

def logout_user(request):
    logout(request)
    return redirect('home')


def about(request):
    return render(request, 'training/about.html', {'menu': menu, 'page_title': 'О сайте'})


class ShowProfile(DataMixin, DetailView):
    model = User
    template_name = 'training/profile.html'
    context_object_name = 'user'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfile, self).get_context_data(*args, **kwargs)
        c_def = self.get_user_context(page_title='Профиль')
        page_user = get_object_or_404(User, pk=self.kwargs['pk'])
        context['login'] = context['user'].username
        context['name'] = context['user'].first_name
        context['last_name'] = context['user'].last_name
        context['weight'] = context['user'].profile.weight
        context['height'] = context['user'].profile.height
        context['email'] = context['user'].email
        context['date_of_birth'] = context['user'].profile.date_of_birth
        return dict(list(context.items()) + list(c_def.items()))
        
    