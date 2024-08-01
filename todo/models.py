from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    list_name = models.CharField(max_length=200, unique=False)
    due_by = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    user_ID = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lists"
    )

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.list_name} | created by {self.user_ID}"


class Task(models.Model):
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    list_ID = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="tasks"
    )

    def __str__(self):
        return f"{self.list_ID} | {self.task_description}"