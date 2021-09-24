from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet

router = DefaultRouter()
router.register('task', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls))
]
