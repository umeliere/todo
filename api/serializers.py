from rest_framework import serializers
from main.models import Tasks, Category


class TasksSerializer(serializers.ModelSerializer):
    """
    Serializer for the model Tasks
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Tasks
        fields = ['id', 'title', 'content', 'category', 'is_done', 'user', 'category', 'created', 'updated']


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the model Category
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Category
        fields = ['id', 'title', 'user']
