from .models import Task
from dataclasses import fields
from django.forms import ModelForm, Textarea, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["type", "title", "task", "deadline"]
        widgets = {"type": Textarea(attrs=
                                     {'class': 'form-control',
                                      'placeholder': 'Тип'}),
                   "title": Textarea(attrs=
                                      {'class': 'form-control',
                                       'placeholder': 'Название'}),
                   "task": Textarea(attrs=
                                     {'class': 'form-control',
                                      'placeholder': 'Описание'}),
                   "deadline": Textarea(attrs=
                                         {'class': 'form-control',
                                          'placeholder': 'Сроки выполнения'})}
