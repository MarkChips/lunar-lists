from django import forms
from .models import List, Task


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('list_name', 'due_by')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_description',)
