from django import template
from paginas.models import Page
#esto es para registrar a libreria      
register = template.Library()

#usamos este decorador para agregarle la
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages