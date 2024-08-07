from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name='home'),
    path('lists/', views.list_view, name='list_view'),
    path('lists/<int:list_id>/', views.task_view, name='task_view'),
    path('lists/<int:list_id>/create/', views.create_task, name='create_task'),
    path('lists/<int:list_id>/delete/', views.list_delete, name='list_delete'),
    path('lists/<int:list_id>/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('lists/<int:list_id>/<int:task_id>/edit/', views.edit_task, name='edit_task'),
]