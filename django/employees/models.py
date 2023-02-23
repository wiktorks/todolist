from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    month_salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name}"


class Task(models.Model):
    description = models.TextField()
    status = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    planned_end_date = models.DateField()
    assigned_worker = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="tasks"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.planned_end_date}"
