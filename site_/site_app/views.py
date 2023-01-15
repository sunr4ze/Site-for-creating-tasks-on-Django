from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'site_app/index.html', {'title': 'Главная страница', 'tasks': tasks})

def create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'site_app/create.html', {'title': 'Создать новую задачу'})

def contacts(request):
    return render(request, 'site_app/contacts.html')