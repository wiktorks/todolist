from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin

from .forms import EmployeeForm
from .models import Employee, Task


class EmployeeListView(FormMixin, ListView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_list.html"
    context_object_name = "employees"


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ["name", "surname", "position", "month_salary"]
    success_url = reverse_lazy("employee-list")


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employees/employee_detail.html"
    context_object_name = "employee"


class TaskListView(ListView):
    template_name = "employees/employee_tasks.html"

    def get_queryset(self):
        self.assigned_worker = get_object_or_404(Employee, pk=self.kwargs["pk"])
        return Task.objects.filter(assigned_worker=self.assigned_worker)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employee"] = self.assigned_worker
        return context


employee_list = EmployeeListView.as_view()
employee_create = EmployeeCreateView.as_view()
employee_detail = EmployeeDetailView.as_view()

task_list = TaskListView.as_view()
