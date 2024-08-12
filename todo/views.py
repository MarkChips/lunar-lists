from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import List, Task
from .forms import ListForm, TaskForm


class HomePage(TemplateView):
    """
    Displays home page.
    """
    template_name = 'todo/index.html'


class Account(TemplateView):
    """
    Displays account settings page.
    """
    template_name = 'todo/account_settings.html'


@login_required
def list_view(request):
    """
    Display :model:`todo.List`. Create a new List.

    **Context**
    ``lists``
        All :model:`todo.List` created by request user.
    ``list_form``
        An instance of :form:`todo.ListForm`.

    **Template:**
    :template:`todo/saved_lists.html`
    """
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


@login_required
def list_delete(request, list_id):
    """
    Delete an instance of :model:`todo.List` belonging to request user,
    then redirect to :template:`todo/saved_lists.html`.
    """
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
def create_task(request, list_id):
    """
    Create an instance of :model:`todo.Task`.

    **Context**
    ``list``
        An instance of :model:`todo.List`.
    ``tasks``
        All :model:`todo.Task` belonging to parent list.
    ``task_form``
        An instance of :form:`todo.TaskForm`.

    **Template:**
    :template:`todo/create_task.html`
    """
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
def task_delete(request, list_id, task_id):
    """
    Delete an instance of :model:`todo.Task` belonging to request user,
    then redirect to :template:`todo/create_task.html`.
    """
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
    """
    Update an instance of :model:`todo.Task`.

    **Context**
    ``form``
        An instance of :form:`todo.TaskForm`.
    ``list``
        A parent instance of :model:`todo.List`.
    ``task``
        An instance of :model:`todo.Task`.

    **Template:**
    :template:`todo/edit_task.html`
    """
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
    """
    Display all tasks belonging to a list. 
    Mark a task as completed.

    **Context**
    ``list``
        An instance of :model:`todo.List`.
    ``tasks``
        All :model:`todo.Task` belonging to parent list.

    **Template:**
    :template:`todo/task_view.html`
    """
    list_instance = get_object_or_404(
        List,
        id=list_id,
        user=request.user
    )

    tasks = list_instance.tasks.all()

    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        try:
            task = Task.objects.get(id=task_id, list=list_instance)
            is_completed = 'is_completed' in request.POST
            task.is_completed = is_completed
            task.save()
        except Task.DoesNotExist:
            print(f"Task with id {task_id} does not exist.")
        return redirect('task_view', list_id=list_id)

    return render(request, 'todo/task_view.html', {
        'list': list_instance,
        'tasks': tasks,
    })


@login_required
def delete_user(request, user_id):
    """
    Delete user's account.

    **Context**
    ``user``
        An instance of :model:`auth.User`.

    **Template:**
    :template:`todo/index.html`
    """
    user = get_object_or_404(User, id=user_id)

    if request.user != user:
        messages.ERROR(
            request, "You don't have permission to delete this account.")
        return redirect('todo/account_settings.html')

    if request.method == 'POST':
        user.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Your account has been successfully deleted.')
        return redirect('home')

    return render(request, 'home', {'user': user})
