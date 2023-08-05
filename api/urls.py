from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CategoryViewSet, TasksViewSet


router = DefaultRouter()
router.register(r"tasks", TasksViewSet, basename='tasks')
router.register(r"categories", CategoryViewSet, basename='categories')


urlpatterns = [
    path("", include(router.urls)),
]
