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
            is_completed=False,
            list=self.list
        )
        self.task.save()

    def login(func):
        def wrapper(self):
            self.client.login(
                username='myUsername',
                password='myPassword'
            )
            func(self)
        return wrapper

    @login
    def test_render_list_view_with_list_form(self):
        response = self.client.get(reverse('list_view'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'List name', response.content)
        self.assertIn(b'Oct. 3, 1995', response.content)
        self.assertIsInstance(response.context['list_form'], ListForm)

    @login
    def test_successful_list_creation(self):
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

    @login
    def test_create_task(self):
        task_data = {
            'task_description': 'New task',
            'list': self.list
        }
        response = self.client.post(
            reverse('create_task', args=[self.list.id]), task_data, follow=True)
        self.assertTrue(Task.objects.filter(task_description='New task',
                        list=self.list).exists())
        self.assertIn(b'Task added to lunar list!', response.content)

    @login
    def test_task_delete(self):
        response = self.client.post(
            reverse('task_delete', args=[self.list.id, self.task.id]), follow=True)
        self.assertRedirects(response, reverse(
            'create_task', args=[self.list.id]))
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
        self.assertIn(b'Task removed', response.content)

    @login
    def test_edit_task(self):
        response = self.client.post(reverse('edit_task', args=[self.list.id, self.task.id]), {
            'task_description': 'Updated task',
            'list': self.list
        }, follow=True)
        self.task.refresh_from_db()
        self.assertEqual(self.task.task_description, 'Updated task')
        self.assertRedirects(response, reverse(
            'create_task', args=[self.list.id]))
        self.assertIn(b'Lunar list entry updated!', response.content)

    @login
    def test_task_view_mark_completed(self):
        response = self.client.post(reverse('task_view', args=[self.list.id]), {
            'task_id': self.task.id,
            'is_completed': True
        }, follow=True)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)
        self.assertRedirects(response, reverse(
            'task_view', args=[self.list.id]))

    @login
    def test_list_delete(self):
        response = self.client.post(
            reverse('list_delete', args=[self.list.id]), follow=True)
        self.assertRedirects(response, reverse('list_view'))
        self.assertFalse(List.objects.filter(id=self.list.id).exists())
        self.assertIn(b'List deleted successfully', response.content)
