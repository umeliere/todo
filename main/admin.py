from django.contrib import admin
from .models import *


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        if not change:
            obj.user = request.user

        super(TasksAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        if not change:
            obj.user = request.user

        super(CategoryAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )