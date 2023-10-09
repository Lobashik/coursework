from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from django import forms
from .models import *


class AddTrainForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['train_name', 'slug', 'content', 'exercises']
        widgets = {
            'train_name': forms.TextInput(attrs={'class': 'form-input', 'id': 'train-name', 'onkeyup': "javascript:document.getElementById('train-slug').value = toTranslit(this.value)"}),
            'content': forms.Textarea(attrs={'rows': 2, 'cols': 27}),
            'slug': forms.TextInput(attrs={'class': 'form-input', 'id': 'train-slug'}),
            'exercises': forms.SelectMultiple(attrs={'class': 'chose-exercise'})
        }
    
    def clean_train_name(self):
        train_name = self.cleaned_data['train_name']
        if len(train_name) > 200:
            raise forms.ValidationError('Длина заголовка превышает 200 символов')
        return train_name
    

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'classs': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    date_of_birth = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'class': 'form-imput', 'type': 'date', 'id': 'register'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'date_of_birth', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))