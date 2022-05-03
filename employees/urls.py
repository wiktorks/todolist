from django.urls import path
from .views import employee_list, employee_create

urlpatterns = [
    path("", employee_list, name="employee-list"),
    path("employee/create", employee_create, name="employee-create"),
]
