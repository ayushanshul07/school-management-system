from django import template
from accounts.models import Student
  
register = template.Library()

@register.filter
def in_category(things, category):
    return things.filter(standard=category)