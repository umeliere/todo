from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, DetailView
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'main/home.html')


@login_required()
def feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(f"{form.cleaned_data['subject']} от {form.cleaned_data['email']}",
                             form.cleaned_data['content'], 'umeliere.answer@yandex.ru', ['umeliere@yandex.ru'])
            if mail:
                messages.success(request, 'Письмо успешно отправлено')
                return redirect('feedback')
            else:
                form.add_error('__all__', 'Ошибка отправки письма')
        else:
            form.add_error('__all__', 'Ошибка валидации')
    else:
        form = ContactForm()
    return render(request, 'main/feedback.html', {'form': form})


class ProfilePageView(ListView):
    template_name = 'main/profile.html'
    context_object_name = 'tasks'
    paginate_by = 4
    model = Tasks

    # def get_queryset(self):
    #     return Tasks.objects.filter(account=self.request.user)


class TaskView(DetailView):
    model = Tasks
    template_name = 'main/task_detail.html'
    context_object_name = 'task_item'


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'main/add_task.html'


class TaskUpdateView(UpdateView):
    model = Tasks
    form_class = TaskUpdateForm
    template_name = 'main/task_update.html'


class TaskDeleteView(DeleteView):
    model = Tasks
    fields = ['title', 'content', 'category']
    template_name = 'main/task_delete.html'
    context_object_name = 'task_item'
    success_url = '/profile/'


class SearchView(ListView):
    template_name = 'main/search.html'
    context_object_name = 'tasks'
    paginate_by = 4

    def get_queryset(self):
        return Tasks.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context


class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'main/add_category.html'
    success_url = '/profile'


class CategoryView(ListView):
    template_name = 'main/profile.html'
    context_object_name = 'tasks'
    paginate_by = 4

    def get_queryset(self):
        return Tasks.objects.filter(category_id=self.kwargs['pk'])
