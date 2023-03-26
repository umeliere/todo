from django.urls import re_path, path, include
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('profile/', login_required(ProfilePageView.as_view()), name='profile'),
    path('feedback/', feedback, name='feedback'),
    path('profile/task/<int:pk>/', TaskView.as_view(), name='view_task'),
    path('profile/add_task/', TaskCreateView.as_view(), name='add_task'),
    path('profile/task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('profile/task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('profile/search/', SearchView.as_view(), name='search'),
]
