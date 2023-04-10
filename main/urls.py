from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('feedback/', feedback, name='feedback'),
    path('profile/', login_required(ProfilePageView.as_view()), name='profile'),
    path('profile/task/<int:pk>/', login_required(TaskView.as_view()), name='view_task'),
    path('profile/add_task/', login_required(TaskCreateView.as_view()), name='add_task'),
    path('profile/task/<int:pk>/update/', login_required(TaskUpdateView.as_view()), name='task_update'),
    path('profile/task/<int:pk>/delete/', login_required(TaskDeleteView.as_view()), name='task_delete'),
    path('profile/<int:pk>/done/', done, name='done'),
    path('profile/search/', login_required(SearchView.as_view()), name='search'),
    path('profile/add_category/', login_required(CategoryCreateView.as_view()), name='add_category'),
    path('profile/category/<int:pk>/', login_required(CategoryView.as_view()), name='category'),
]
