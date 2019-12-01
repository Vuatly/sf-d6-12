from django import template
register = template.Library()

@register.filter
def create_range(value, start_index=0):
    return range(start_index, value+start_index)

@register.filter
def division_on_three(value):
    if value % 3 == 0:
        return value