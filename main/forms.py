from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Не выбрано"

    class Meta:
        model = Tasks
        fields = ['title', 'content', 'category']


class ContactForm(forms.Form):
    subject = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(label='Ваша почта', widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    content = forms.CharField(label='Обращение', widget=forms.Textarea(attrs={
        'class': 'form-control', 'rows': 8
    }))


