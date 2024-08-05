from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name='home'),
    path('lists/', login_required(views.list_view), name='list_view'),
]