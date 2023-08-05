from rest_framework import viewsets
from api.serializers import TasksSerializer, CategorySerializer
from api.permissions import IsOwnerOrReadOnly
from main.models import Tasks, Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from api.service import TaskFilter, TasksApiPagination


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter
    pagination_class = TasksApiPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
