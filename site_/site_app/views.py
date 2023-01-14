from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'site_app/index.html', {'title': 'Главная страница', 'tasks': tasks})

def about(request):
    return render(request, 'site_app/about.html')

def contacts(request):
    return render(request, 'site_app/contacts.html')