from rest_framework.routers import DefaultRouter
from .views import CategoryView, TasksView

router = DefaultRouter()
router.register(r"tasks", TasksView, basename='tasks')
router.register(r"category", CategoryView, basename='category')
