from rest_framework import serializers
from .models import Task

class TaskSrl(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = "__all__"
    read_only_fields = ("deleted_at", "created_at", "updated_at")