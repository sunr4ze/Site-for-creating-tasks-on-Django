from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'site_app/index.html')

def about(request):
    return render(request, 'site_app/about.html')

def contacts(request):
    return HttpResponse("<h1>Контакты</h1>")