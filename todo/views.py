from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import List

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'todo/index.html'

@login_required
def list_view(request):
    user_lists = List.objects.filter(user_ID=request.user)

    return render(request, 'todo/todo_list.html', {'lists': user_lists})