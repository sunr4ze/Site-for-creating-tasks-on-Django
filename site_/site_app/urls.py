from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('task-creating/', views.create),
    path('contacts/', views.contacts),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]
