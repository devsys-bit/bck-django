from django.urls import path
from . import views

urlpatterns = [
  path('task/', views.ListTask.as_view(), name='task-list'),
  path('task/<int:pk>/', views.DetailTask.as_view(), name='task-detail'),
  path('task/create/', views.CreateTask.as_view(), name='task-create'),
  path('task/update/<int:pk>/', views.UpdateTask.as_view(), name='task-update'),
  path('task/remove/<int:pk>/', views.DeleteTask.as_view(), name='task-delete'),
  path('task/restore/<int:pk>/', views.RestoreTask.as_view(), name='task-restore'),
]
