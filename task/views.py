from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from cmn.util import findPagination
from .models import Task
from .serializers import TaskSrl
from .filters import TaskFilter

class ListTask(generics.ListAPIView):
  queryset = Task.objects.all().filter(deleted_at__isnull=True)
  serializer_class = TaskSrl
  pagination_class = findPagination
  filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
  filterset_class = TaskFilter
  ordering_fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
  search_fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
  ordering = ['id']

class DetailTask(generics.RetrieveAPIView):
  queryset = Task.objects.filter(deleted_at__isnull=True)
  serializer_class = TaskSrl

class CreateTask(generics.CreateAPIView):
  queryset = Task.objects.filter(deleted_at__isnull=True)
  serializer_class = TaskSrl

class UpdateTask(generics.UpdateAPIView):
  queryset = Task.objects.filter(deleted_at__isnull=True)
  serializer_class = TaskSrl

class DeleteTask(generics.UpdateAPIView):
  queryset = Task.objects.filter(deleted_at__isnull=True)
  serializer_class = TaskSrl
  http_method_names = ['patch']

class RestoreTask(generics.UpdateAPIView):
  queryset = Task.objects.filter(deleted_at__isnull=True)
  serializer_class = TaskSrl
  http_method_names = ['patch']