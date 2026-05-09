from django import template

register = template.Library()


@register.filter
def split(value, sep=','):
    if not value:
        return []
    return [t.strip() for t in value.split(sep) if t.strip()]
