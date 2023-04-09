from rest_framework import viewsets
from .serializers import TasksSerializer, CategorySerializer
from .permissions import *
from main.models import Tasks, Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TasksView(viewsets.ModelViewSet):
    throttle_scope = 'low_request'

    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


class CategoryView(viewsets.ModelViewSet):
    throttle_scope = 'low_request'

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
