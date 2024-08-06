from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import List, Task

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'todo/index.html'

@login_required
def list_view(request):
    user_lists = List.objects.filter(user=request.user)

    return render(request, 'todo/saved_lists.html', {'lists': user_lists})

@login_required
def task_view(request, list_id):
    list_instance = get_object_or_404(List, id=list_id, user=request.user)

    tasks = list_instance.tasks.all()

    return render(request, 'todo/task_view.html', {
        'list': list_instance,
        'tasks': tasks,
    })