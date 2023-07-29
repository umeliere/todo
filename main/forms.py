from django import forms
from main.models import Category, Tasks


class TaskForm(forms.ModelForm):
    """
    Форма для создания задания
    """
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)
        self.fields['category'].empty_label = "Не выбрано"

    class Meta:
        model = Tasks
        fields = ['title', 'content', 'category']


class TaskUpdateForm(forms.ModelForm):
    """
    Форма для обновления задания
    """
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)
        self.fields['category'].empty_label = "Не выбрано"

    class Meta:
        model = Tasks
        fields = ['title', 'content', 'category']


class CategoryForm(forms.ModelForm):
    """
    Форма для создания категории
    """
    class Meta:
        model = Category
        fields = ['title']

