from .models import Task
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["type", "title", "task", "priority", "deadline", "status"]