from django.urls import path
from main.views import (
    home,
    ProfilePageView,
    TaskView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    SearchView,
    CategoryView,
    CategoryCreateView,
    IsDoneView
)


urlpatterns = [
    path('', home, name='home'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('profile/task/<int:pk>/', TaskView.as_view(), name='view_task'),
    path('profile/add_task/', TaskCreateView.as_view(), name='add_task'),
    path('profile/task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('profile/task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('profile/<int:pk>/done/', IsDoneView.as_view(), name='done'),
    path('profile/search/', SearchView.as_view(), name='search'),
    path('profile/add_category/', CategoryCreateView.as_view(), name='add_category'),
    path('profile/category/<int:pk>/', CategoryView.as_view(), name='category'),
]
