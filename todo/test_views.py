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

    def test_render_list_view_with_list_form(self):
        self.client.login(
            username='myUsername',
            password='myPassword'
        )
        response = self.client.get(reverse('list_view'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'List name', response.content)
        self.assertIn(b'Oct. 3, 1995', response.content)
        self.assertIsInstance(response.context['list_form'], ListForm)

    def test_successful_list_creation(self):
        self.client.login(
            username='myUsername',
            password='myPassword'
        )
        list_data = {
            'list_name': 'New list',
            'due_by': '2025-05-10'
        }
        response = self.client.post(
            reverse('list_view'), list_data, follow=True)
        # Check redirect chain
        self.assertEqual(response.status_code, 200)
        # Check that the list was created in the database
        self.assertTrue(List.objects.filter(
            list_name='New list', user=self.user).exists())
        # Check for the success message
        self.assertIn(b'New lunar list created!', response.content)
