from django.urls import path
from . import views

urlpatterns = [
    path("tasks/<int:pk>/update/", views.update_task_api_view, name="api-task-update")
]
