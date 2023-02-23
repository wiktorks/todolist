from django import forms
from django.core.validators import RegexValidator
from .models import Employee, Task


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=100,
                           validators=[RegexValidator(r'^[a-zA-Z]+$', message='Imie musi się składać z samych liter')])
    surname = forms.CharField(max_length=100, validators=[
        RegexValidator(r'^[a-zA-Z]+$', message='Nazwisko musi się składać z samych liter')])

    class Meta:
        model = Employee
        fields = ["name", "surname", "position", "month_salary"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "description",
            "status",
            "category",
            "planned_end_date",
            "is_completed",
        ]
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
