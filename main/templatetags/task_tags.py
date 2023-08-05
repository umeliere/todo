from django import template

from main.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    """
    Get all the categories function
    """
    return Category.objects.all()
