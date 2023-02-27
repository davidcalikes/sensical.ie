from django import template
register = template.Library()


@register.filter(name='split')
def split_filter(text, delimiter):
    return text.split(delimiter)
