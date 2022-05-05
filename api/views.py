from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

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


update_task_api_view = UpdateTaskView.as_view()
list_tasks_today_api_view = EmployeeTaskTodayListView.as_view()
