from django.shortcuts import (
    get_object_or_404,
    redirect,
    render, 
) 
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import List, Task
from .forms import ListForm, TaskForm

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'todo/index.html'

@login_required
def list_view(request):
    user_lists = List.objects.filter(user=request.user)

    if request.method == 'POST':
        list_form = ListForm(data=request.POST)
        if list_form.is_valid():
            list = list_form.save(commit=False)
            list.user = request.user
            list.save()
            return redirect('create_task', list_id=list.id)

    list_form = ListForm()

    return render(request, 'todo/saved_lists.html', {
        'lists': user_lists,
        'list_form': list_form,
    })

def create_task(request, list_id):
    list_instance = get_object_or_404(
        List, 
        id=list_id, 
        user=request.user
    )

    tasks = list_instance.tasks.all()

    if request.method == 'POST':
        task_form = TaskForm(data=request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.list = list_instance
            task.save()

    task_form = TaskForm()

    return render(request, 'todo/create_task.html', {
        'list': list_instance,
        'tasks': tasks,
        'task_form': task_form,
    })

@login_required
def task_view(request, list_id):
    list_instance = get_object_or_404(
        List, 
        id=list_id, 
        user=request.user
    )

    tasks = list_instance.tasks.all()

    return render(request, 'todo/task_view.html', {
        'list': list_instance,
        'tasks': tasks,
    })