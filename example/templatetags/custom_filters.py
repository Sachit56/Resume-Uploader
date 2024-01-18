from django import template
import re

register=template.Library()

@register.filter
def remove_special_characters(value):
    return re.sub(r'[^\w\s,]', '', value)