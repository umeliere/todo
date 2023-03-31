from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class Tasks(models.Model):
    title = models.CharField(max_length=75, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Описание задачи")
    is_done = models.BooleanField(verbose_name='Выполнено?', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Время обновления")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, verbose_name='Категория', null=True)
    # account = models.ForeignKey(User,  on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('view_task', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Задания"
        ordering = ['created']


class Category(models.Model):
    title = models.CharField(max_length=30, db_index=True, verbose_name="Название категории")

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Категории"
