from django import forms
from main.models import Category, Tasks


class TaskForm(forms.ModelForm):
    """
    Create the task form
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
    Update the task form
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
    Create the category form
    """
    class Meta:
        model = Category
        fields = ['title']

