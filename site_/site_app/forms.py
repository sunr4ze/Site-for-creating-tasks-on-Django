from .models import Task
from dataclasses import fields
from django.forms import ModelForm, Textarea, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["type", "title", "task", "priority", "deadline", "status"]
        widgets = {"type": Textarea(attrs=
                                     {'class': 'form-control',
                                      'placeholder': 'Тип'}),
                   "title": Textarea(attrs=
                                      {'class': 'form-control',
                                       'placeholder': 'Название'}),
                   "task": Textarea(attrs=
                                     {'class': 'form-control',
                                      'placeholder': 'Описание'}),
                   "priority": Textarea(attrs=
                                         {'class': 'form-control',
                                          'placeholder': 'Приоритет'}),
                   "deadline": Textarea(attrs=
                                         {'class': 'form-control',
                                          'placeholder': 'Сроки выполнения'}),
                   "status": Textarea(attrs=
                                       {'class': 'form-control',
                                        'placeholder': 'Статус'})}
