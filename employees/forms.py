from django import forms
from .models import Employee, Task


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "surname", "position", "month_salary"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "category", "planned_end_date"]
        widgets = {
            "planned_end_date": forms.DateInput(
                format=("%m/%d/%Y"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }
