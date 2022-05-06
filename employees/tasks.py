from celery import shared_task
import csv
from .models import Employee


@shared_task
def import_employees_from_csv_file(csv_file):
    Employee.objects.all()
