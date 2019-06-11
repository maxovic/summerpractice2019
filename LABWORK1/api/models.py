from django.db import models
from datetime import date
# Create your models here.


class TaskList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField(default=date(2020, 3, 14))
    status = models.CharField(max_length=100)
    task_list = models.ForeignKey(TaskList, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


