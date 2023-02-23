from to_do_list.celery import app
import csv
from .models import Employee


@app.task
def import_employees_from_csv_file(csv_file):
    with open(csv_file["path"], mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        if set(reader.fieldnames) != set(
            ["name", "surname", "position", "month_salary"]
        ):
            return -1
        employees = list(
            map(lambda employee_dict: Employee(**employee_dict), list(reader))
        )
        print(f"celery: {employees}")
        Employee.objects.all().delete()
        Employee.objects.bulk_create(employees)
    return 1
