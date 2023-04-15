from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TasksViewSet, UserViewSet


router = DefaultRouter()
router.register(r"tasks", TasksViewSet, basename='tasks')
router.register(r"category", CategoryViewSet, basename='category')
router.register(r"users", UserViewSet, basename='users')
