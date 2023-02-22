from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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
    @swagger_auto_schema(
        operation_description="Download list of employees with their corresponding tasks which deadline ends today",
        responses={200: EmployeeSerializer},
    )
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
        if not employee_list:
            raise Exception('Babol nr 1')

        return Response(employee_list)


response_schema_dict = {
    "200": openapi.Response(
        description="returns generated csv file with list of tasks belonging to given employee",
        examples={
            "application/text": """id,description,status,category,planned_end_date,created_at,is_completed,assigned_worker\n
            14,desc,stat,cat,2022-05-06,2022-05-04...,False,9"""
        },
    )
}


@swagger_auto_schema(
    method="GET",
    operation_description="Download list of tasks belonging to given employee",
    responses=response_schema_dict,
)
@api_view(["GET"])
def get_tasks_csv_file(request, pk):
    tasks = Task.objects.filter(assigned_worker__pk=pk)
    if tasks:
        task_serializer = TaskSerializer(tasks, many=True)
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
