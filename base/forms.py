from django.forms import ModelForm
from .models import Task

class AddTask(ModelForm):
    class Meta:
        model=Task
        fields=["task"] #form includes task name only


class editTask(ModelForm):
    class Meta:
        model=Task
        fields=["task"]