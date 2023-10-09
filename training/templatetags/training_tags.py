from django import template
from training.models import *

register = template.Library()

@register.simple_tag()
def get_information():
    return Training.objects.all()