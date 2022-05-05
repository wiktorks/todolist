from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.views.generic.edit import FormMixin

from .forms import EmployeeForm, TaskForm
from .models import Employee, Task


class EmployeeListView(FormMixin, ListView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_list.html"
    context_object_name = "employees"


class EmployeeCreateView(CreateView):
    http_method_names = ["post"]
    model = Employee
    fields = ["name", "surname", "position", "month_salary"]
    success_url = reverse_lazy("employee-list")


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employees/employee_detail.html"
    context_object_name = "employee"


class TaskListView(FormMixin, ListView):
    template_name = "employees/employee_tasks.html"
    form_class = TaskForm

    def get_queryset(self):
        self.assigned_worker = get_object_or_404(Employee, pk=self.kwargs["pk"])
        return Task.objects.filter(assigned_worker=self.assigned_worker)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employee"] = self.assigned_worker
        return context


class TaskCreateView(CreateView):
    http_method_names = ["post"]
    model = Task
    fields = ["description", "status", "category", "planned_end_date", "is_completed"]

    def get_success_url(self):
        employee_id = self.kwargs["pk"]
        return reverse_lazy("employee-tasks", kwargs={"pk": employee_id})

    def form_valid(self, form):
        assigned_worker = Employee.objects.get(pk=self.kwargs["pk"])
        form.instance.assigned_worker = assigned_worker
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    model = Task
    pk_url_kwarg = "task_pk"

    def get_success_url(self):
        employee_id = self.kwargs["pk"]
        return reverse_lazy("employee-tasks", kwargs={"pk": employee_id})


employee_list = EmployeeListView.as_view()
employee_create = EmployeeCreateView.as_view()
employee_detail = EmployeeDetailView.as_view()

task_list = TaskListView.as_view()
task_create = TaskCreateView.as_view()
task_delete = TaskDeleteView.as_view()
