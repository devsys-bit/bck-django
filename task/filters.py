import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
  id = django_filters.BaseInFilter(field_name="id", lookup_expr="in")
  title = django_filters.CharFilter(field_name="title", lookup_expr="istartswith")
  description = django_filters.CharFilter(field_name="description", lookup_expr="istartswith")
  completed = django_filters.BooleanFilter(field_name="completed")
  created_at = django_filters.CharFilter(field_name="created_at", lookup_expr="istartswith")
  updated_at = django_filters.CharFilter(field_name="updated_at", lookup_expr="istartswith")
  create_at_gte = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
  create_at_lte = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")
  update_at_gte = django_filters.DateTimeFilter(field_name="updated_at", lookup_expr="gte")
  update_at_lte = django_filters.DateTimeFilter(field_name="updated_at", lookup_expr="lte")

  class Meta:
    model = Task
    fields = [
      "id",
      "title",
      "description",
      "completed",
      "created_at",
      "updated_at",
      "create_at_gte",
      "create_at_lte",
      "update_at_gte",
      "update_at_lte",
    ]
