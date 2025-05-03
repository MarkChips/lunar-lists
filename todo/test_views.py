from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import ListForm, TaskForm
from .models import List, Task


class TestTodoViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='myUsername',
            password='myPassword',
            email='test@test.com'
        )
        self.list = List(
            list_name='List name',
            due_by='1995-10-03',
            created_on='2025-10-03',
            user=self.user
        )
        self.list.save()

        self.task = Task(
            task_description='Task description',
            is_completed=True,
            list=self.list
        )
        self.task.save()
