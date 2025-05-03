from django.test import TestCase
from .forms import ListForm, TaskForm


class TestListForm(TestCase):

    def test_form_is_valid(self):
        list_form = ListForm({'list_name': 'New List', 'due_by': '1995-10-03'})
        self.assertTrue(list_form.is_valid(), msg='Form is not valid')

    def test_list_name_is_required(self):
        list_form = ListForm({'list_name': '', 'due_by': '1995-10-03'})
        self.assertFalse(list_form.is_valid(
        ), msg='List name was not provided, but the form is valid')

    def test_due_by_is_required(self):
        list_form = ListForm({'list_name': 'New List', 'due_by': ''})
        self.assertFalse(list_form.is_valid(),
                         msg='Due by date was not provided, but the form is valid')


class TestTaskForm(TestCase):

    def test_form_is_valid(self):
        task_form = TaskForm({'task_description': 'Buy milk'})
        self.assertTrue(task_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        task_form = TaskForm({'task_description': ''})
        self.assertFalse(task_form.is_valid(), msg='Form is valid')
