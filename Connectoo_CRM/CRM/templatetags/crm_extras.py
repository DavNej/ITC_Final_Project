from django import template
from django.template import loader
from django.contrib.auth.models import Group
from django.template import Library


register = template.Library()

@register.filter(name='has_group') 
def has_group(user, group_name):
    group =  Group.objects.get(name=group_name) 
    return group in user.groups.all()
    