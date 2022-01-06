from django import template

register = template.Library()

@register.filter(name='replace')
def do_replace(value, agrs):
    oldValue = agrs.split(':')[0]
    print(oldValue)
    newValue = agrs.split(':')[1]
    print(newValue)
    return value.replace(oldValue, newValue)