from django import template

register = template.Library()


@register.filter(name='contains')
def list_contains(lst, val):
    return val in lst
