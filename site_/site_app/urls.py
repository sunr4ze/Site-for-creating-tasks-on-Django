from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('task-creating/', views.create, name='create'),
    path('contacts/', views.contacts),
]
