from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    month_salary = models.DecimalField(max_digits=8, decimal_places=2)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    planned_end_date = models.DateField()
    assigned_worker = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True)
