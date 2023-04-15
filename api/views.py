from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import TasksSerializer, CategorySerializer, UserSerializer
from .permissions import *
from main.models import Tasks, Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TasksViewSet(viewsets.ModelViewSet):
    throttle_scope = 'low_request'

    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    throttle_scope = 'low_request'

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
