from rest_framework.generics import UpdateAPIView

from .serializers import TaskSerializer
from employees.models import Task

# Create your views here.
class UpdateTaskView(UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


update_task_api_view = UpdateTaskView.as_view()
