import markdown

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def convertir_markdown(value):
    return markdown.markdown(value)