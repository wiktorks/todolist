from django.urls import path
from . import views

urlpatterns = [
    path("tasks/<int:pk>/update/", views.update_task_api_view, name="api-task-update"),
    path(
        "employees/tasks/today/",
        views.list_tasks_today_api_view,
        name="api-tasks-today-list",
    ),
]
