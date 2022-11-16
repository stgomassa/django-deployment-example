from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(agr,'')

### ('name of the filter',function)
# register.filter('cut',cut)
