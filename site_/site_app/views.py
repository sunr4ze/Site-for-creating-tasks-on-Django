from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Hello</h4>")

def info(request):
    return HttpResponse("<h1>О нас</h1>")

def contacts(request):
    return HttpResponse("<h1>Контакты</h1>")