from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import TaskForm, TaskUpdateForm, CategoryForm
from main.models import Tasks, Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator


def home(request):
    return render(request, 'main/home.html')


class ProfilePageView(LoginRequiredMixin, ListView):
    """
    Представление для предоставления задач пользователя
    """
    template_name = 'main/profile.html'
    context_object_name = 'tasks'
    paginate_by = 4
    model = Tasks

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Профиль'
        return context

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)


class TaskView(LoginRequiredMixin, DetailView):
    """
    Представление для создания задачи
    """
    model = Tasks
    template_name = 'main/task_detail.html'
    context_object_name = 'task_item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = f'Задание: {self.object.title}'
        return context

    def get_queryset(self):
        return super(TaskView, self).get_queryset(
        ).filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания задачи
    """
    form_class = TaskForm
    template_name = 'main/add_task.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = f'Создание задания'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    Представление для обновления задачи
    """
    model = Tasks
    form_class = TaskUpdateForm
    template_name = 'main/task_update.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = f'Обновление задачи {self.object.title}'
        return context

    def get_queryset(self):
        return super(TaskUpdateView, self).get_queryset(
        ).filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


@method_decorator(require_POST, name='dispatch')
class IsDoneView(UpdateView):
    model = Tasks
    template_name = 'main/profile.html '
    fields = ('is_done',)
    success_url = reverse_lazy('profile')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление удаления задачи
    """
    model = Tasks
    fields = ['title', 'content', 'category']
    template_name = 'main/task_delete.html'
    context_object_name = 'task_item'
    success_url = '/profile/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = f'Удаление задания {self.object.title}'
        return context

    def get_queryset(self):
        return super(TaskDeleteView, self).get_queryset(
        ).filter(user=self.request.user)


class SearchView(LoginRequiredMixin, ListView):
    """
    Представление страницы после поиска
    """
    template_name = 'main/search.html'
    context_object_name = 'tasks'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s', '')
        context['title'] = context['s']
        if not context['s']:
            context["title"] = 'Все товары'
        else:
            context['title'] = f'Задания по запросу: {context["s"]}'

        return context

    def get_queryset(self):
        return Tasks.objects.filter(title__icontains=self.request.GET.get('s', ''), user=self.request.user)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания категории
    """
    form_class = CategoryForm
    template_name = 'main/add_category.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Создание категории'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreateView, self).form_valid(form)


class CategoryView(LoginRequiredMixin, ListView):
    """
    Представление страницы по определенной категории
    """
    template_name = 'main/profile.html'
    context_object_name = 'tasks'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = Category.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Tasks.objects.filter(category_id=self.kwargs['pk'], user=self.request.user)


def page_not_found(request, exception):
    """
    Представление ошибки 404
    """
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    """
    Представление ошибки 500
    """
    return render(request, "misc/500.html", status=500)
