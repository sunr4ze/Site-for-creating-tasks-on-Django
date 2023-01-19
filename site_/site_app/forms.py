from .models import Task
from django.forms import ModelForm, Textarea, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["type", "title", "task", "deadline"]
        widgets = {"type": TextInput(attrs=
                                     {'class': 'form-control',
                                      'placeholder': 'Тип'}),
                   "title": TextInput(attrs=
                                      {'class': 'form-control',
                                       'placeholder': 'Название'}),
                   "task": Textarea(attrs=
                                     {'class': 'form-control',
                                      'placeholder': 'Описание',
                                      'name': 'task'}),
                   "deadline": TextInput(attrs=
                                         {'class': 'form-control',
                                          'placeholder': 'Сроки выполнения'})}
