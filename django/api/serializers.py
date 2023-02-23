from rest_framework.serializers import ModelSerializer
from employees.models import Employee, Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class EmployeeSerializer(ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ["tasks", "name", "surname", "month_salary", "position"]
