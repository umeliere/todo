from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import Tasks, Category


class TasksSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Tasks
        fields = ['id', 'title', 'content', 'category', 'is_done', 'user', 'category', 'created', 'updated']


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Category
        fields = ['id', 'title', 'user']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']
