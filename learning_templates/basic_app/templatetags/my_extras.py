from django import template

register = template.Library()

@register.filter(name='cute')
def cute(value,arg):
    '''
    this cuts out all values of "arg" from the string
    '''
    return value.replace(arg,'')

# register.filter('cute',cute)
