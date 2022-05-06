from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.views.generic.edit import FormMixin
from django.views.decorators.http import require_http_methods

from .forms import EmployeeForm, TaskForm
from .models import Employee, Task
from .tasks import import_employees_from_csv_file


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


class EmployeeDeleteView(DeleteView):
    model = Employee
    pk_url_kwarg = "pk"

    def get_success_url(self):
        return reverse_lazy("employee-list")


class TaskListView(FormMixin, ListView):
    template_name = "employees/employee_tasks.html"
    form_class = TaskForm

    def get_queryset(self):
        self.assigned_worker = get_object_or_404(Employee, pk=self.kwargs["pk"])
        return Task.objects.filter(assigned_worker=self.assigned_worker)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employee"] = self.assigned_worker
        statuses = []
        for task in context["object_list"]:
            if task.status not in statuses:
                statuses.append(task.status)
        context["status_list"] = statuses
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


def store_file(file):
    with open("temp/employees.csv", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


@require_http_methods(["POST"])
def employee_file_upload_view(request):
    try:
        file = request.FILES.get("employee_file", False)
        if file:
            store_file(file)
            file = import_employees_from_csv_file.delay({"path": "temp/employees.csv"})
        response_code = file.get(timeout=1)
        if response_code > 0:
            messages.add_message(
                request, messages.SUCCESS, "Successfully added employees from file"
            )
        else:
            messages.add_message(request, messages.ERROR, "Wrong file format.")
        return redirect("employee-list")
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Wrong file format.")
        return redirect("employee-list")


employee_list = EmployeeListView.as_view()
employee_create = EmployeeCreateView.as_view()
employee_detail = EmployeeDetailView.as_view()
employee_delete = EmployeeDeleteView.as_view()

task_list = TaskListView.as_view()
task_create = TaskCreateView.as_view()
task_delete = TaskDeleteView.as_view()
