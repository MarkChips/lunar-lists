from django.db import models
from django.contrib.auth.models import User
from datetime import date


class List(models.Model):
    """
    Stores a single to-do list related to :model:`auth.User`.
    """
    list_name = models.CharField(max_length=50)
    due_by = models.DateField(default=date.today)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lists"
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.list_name} | created by {self.user}"


class Task(models.Model):
    """
    Stores a single task entry related to :model:`auth.User`
    and :model:`todo.List`.
    """
    task_description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="tasks"
    )

    def __str__(self):
        return f"{self.list} | {self.task_description}"
