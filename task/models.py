from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=50, blank=True, null=True, default="")
  description = models.CharField(max_length=100, blank=True, null=True, default="")
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  deleted_at = models.DateTimeField(blank=True, null=True, default=None)

  class Meta:
    db_table = 'task'
    indexes = [ models.Index(fields=['id'])]