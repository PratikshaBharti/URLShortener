from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def task_view(request):
    return render(request, 'task.html')

def home(request):
    return HttpResponse("this is the home page")
