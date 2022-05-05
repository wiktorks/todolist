from rest_framework.serializers import ModelSerializer
from employees.models import Employee, Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
