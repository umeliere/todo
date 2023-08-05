from django_filters.rest_framework import BaseInFilter, CharFilter, FilterSet
from rest_framework.pagination import PageNumberPagination

from main.models import Tasks


class CharFilterInFilter(BaseInFilter, CharFilter):
    """
    Filter class for multiple uses
    read docs: https://django-filter.readthedocs.io/en/stable/ref/filters.html
    """
    pass


class TasksApiPagination(PageNumberPagination):
    """
    Modified pagination class for Tasks model
    """
    page_size = 4


class TaskFilter(FilterSet):
    """
    Filter class for filter by category
    """
    category = CharFilterInFilter(field_name='category__title', lookup_expr='in')

    class Meta:
        model = Tasks
        fields = ('category',)
