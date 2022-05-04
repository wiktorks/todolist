from django.urls import path
from employees import views

urlpatterns = [
    path("", views.employee_list, name="employee-list"),
    path("employee/create/", views.employee_create, name="employee-create"),
    path("employee/<int:pk>", views.employee_detail, name="employee-details"),
    path("employee/<int:pk>/tasks", views.task_list, name="employee-tasks"),
]
