
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_view, name='task'),
    path('home', views.home, name='home'),
]  
