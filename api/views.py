from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import datetime
import csv
from io import StringIO

from .serializers import TaskSerializer, EmployeeSerializer
from employees.models import Task, Employee

# Create your views here.
class UpdateTaskView(UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class EmployeeTaskTodayListView(APIView):
    def get(self, request, format=None):
        employees = Employee.objects.filter(
            tasks__planned_end_date=datetime.date.today()
        ).distinct()
        employees_serializer = EmployeeSerializer(employees, many=True, source="tasks")
        employee_list = [
            {
                "tasks": list(
                    filter(
                        lambda task: task["planned_end_date"]
                        == datetime.datetime.today().strftime("%Y-%m-%d"),
                        task_list.pop("tasks"),
                    )
                ),
                **dict(task_list),
            }
            for task_list in employees_serializer.data
        ]

        return Response(employee_list)


@api_view()
def get_tasks_csv_file(request, pk):
    tasks = Task.objects.filter(assigned_worker__pk=pk)
    if tasks:
        task_serializer = TaskSerializer(tasks, many=True)
        print(tasks.first().description)
        print(tasks.first().is_completed)
        fieldnames = task_serializer.data[0].keys()
        sio = StringIO()
        writer = csv.DictWriter(sio, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()
        writer.writerows(task_serializer.data)

        response = HttpResponse(
            sio.getvalue(), content_type="application/text charset=utf-8"
        )
        response["Content-Disposition"] = f'attachment; filename="foo.csv"'
        return response

    return Response({"ni": "mo"})


update_task_api_view = UpdateTaskView.as_view()
list_tasks_today_api_view = EmployeeTaskTodayListView.as_view()
