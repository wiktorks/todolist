from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin

from .forms import EmployeeForm
from .models import Employee


class EmployeeListView(FormMixin, ListView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_list.html"
    context_object_name = "employees"


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ["name", "surname", "position", "month_salary"]
    success_url = reverse_lazy("employee-list")


employee_list = EmployeeListView.as_view()
employee_create = EmployeeCreateView.as_view()
