from django import template

register = template.Library()


@register.filter(name='mytitle')
def mytitle(value):
    """
    title and add string
    """
    return value.title()

#register.filter('cutt', cutt)

def cun(value, arg):
    """
    Cuts off arg from the value
    """
    return value.replace(arg," ")

register.filter('cun', cun)