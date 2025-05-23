from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    ...

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed']  # Now you can filter by ?completed=true or false
