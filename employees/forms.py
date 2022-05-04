from django.forms import ModelForm
from .models import Employee, Task


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "surname", "position", "month_salary"]


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "category", "planned_end_date"]
