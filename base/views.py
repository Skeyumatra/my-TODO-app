from django.shortcuts import render, redirect
from .forms import TaskForm
from . import models
# Create your views here.
def homePage(request):
    tasks=models.Task.objects.all()
    return render(request,"home.html",{"tasks":tasks})

def addTask(request):
    task=TaskForm()
    if request.method=="POST":
        task=TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect("home")
    else:
        task=TaskForm()
    return render(request,"addTask.html",{"task":task})
