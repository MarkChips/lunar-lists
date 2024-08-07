from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
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
            messages.add_message(
                request, messages.SUCCESS, 'New lunar list created!'
            )
            return redirect('create_task', list_id=list.id)
        else:
            print(list_form.errors)

    else:
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
            messages.add_message(
                request, messages.SUCCESS, 'Task added to lunar list!'
            )

    else:
        task_form = TaskForm()

    return render(request, 'todo/create_task.html', {
        'list': list_instance,
        'tasks': tasks,
        'task_form': task_form,
    })

@login_required
def list_delete(request, list_id):
    list_instance = get_object_or_404(
        List, 
        id=list_id, 
        user=request.user
    )

    list_instance.delete()
    messages.add_message(
                request, messages.SUCCESS, 'List deleted successfully'
            )

    return redirect('list_view')

@login_required
def task_delete(request, list_id, task_id):
    list_instance = get_object_or_404(
        List, 
        id=list_id, 
        user=request.user
    )
    task = get_object_or_404(
        Task, 
        id=task_id, 
        list=list_instance
    )

    task.delete()
    messages.add_message(
                request, messages.SUCCESS, 'Task removed'
            )

    return redirect('create_task', list_id=list_id)

@login_required
def edit_task(request, list_id, task_id):
    list_instance = get_object_or_404(
        List, 
        id=list_id, 
        user=request.user
    )
    task = get_object_or_404(
        Task, 
        id=task_id, 
        list=list_instance
    )

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Lunar list entry updated!'
            )
            return redirect('create_task', list_id=list_id)
    else:
        form = TaskForm(instance=task)

    return render(request, 'todo/edit_task.html', {
        'form': form,
        'list': list_instance,
        'task': task,
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