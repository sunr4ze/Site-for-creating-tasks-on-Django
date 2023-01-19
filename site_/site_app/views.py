from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    context = {'tasks': tasks}
    return render(request, 'site_app/index.html', context)


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Задача успешно добавлена!')
        else:
            messages.error(request, 'Не удалось создать задачу')

    form = TaskForm()
    context = {'form': form}
    return render(request, 'site_app/create.html', context)


def contacts(request):
    return render(request, 'site_app/contacts.html')


def edit(request, id):
    tasks = Task.objects.get(id=id)
    try:
        if request.method == "POST":
            tasks.type = request.POST.get("type")
            tasks.title = request.POST.get("title")
            tasks.deadline = request.POST.get("deadline")
            tasks.task = request.POST.get("task")
            tasks.save()
            return HttpResponseRedirect("/")
        else:
            context = {'tasks': tasks}
            return render(request, "edit.html", context)
    except tasks.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def delete(request, id):
    tasks = Task.objects.get(id=id)
    tasks.delete()
    messages.success(request, 'Задача  удалена')
    return HttpResponseRedirect('/')

