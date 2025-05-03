from django.test import TestCase
from .forms import ListForm


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
