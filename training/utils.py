from .models import *


menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Упражнения", 'url_name': 'exercises'},
        {'title': "Тренировки", 'url_name': 'trains'},
        {'title': "О сайте", 'url_name': 'about'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context