from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name='home'),
    path('lists/', login_required(views.list_view), name='list_view'),
    path('lists/<int:list_id>/', login_required(views.task_view), name='task_view'),
    path('lists/create/', views.create_task, name='create_task')
]