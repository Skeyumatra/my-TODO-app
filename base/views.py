from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.
def homePage(request):
    tasks=models.Task.objects.all()  #pulling tasks row from db
    return render(request,"home.html",{"tasks":tasks})

def AddTask(request):
    task=forms.AddTask() #provide the form
    if request.method=="POST":
        task=forms.AddTask(request.POST) #taking input
        if task.is_valid():
            task.save()   #adding to db task row
            return redirect("home") #back to the home
    else:
        task=forms.AddTask()
    return render(request,"addTask.html",{"task":task})


def editTaskName(request,pk):
    form=forms.editTask() #provide the form
    if request.method=="POST":
        form=forms.editTask(request.POST)
        if form.is_valid():
            task = models.Task.objects.get(pk=pk) #taking the task object that its id=pk
            task.task=form.cleaned_data["task"]
            task.save()    #changing to edited version and saving to db
            return redirect("/")
    return render(request,"editTask.html",{"form":form})


def achieveTask(request,pk):
    task=models.Task.objects.get(pk=pk) #getting the selected object
    if task.isAchieved:
        task.isAchieved=False   #if task is achieved, mark as not achieved
        task.save()
    else:
        task.isAchieved=True    #if task isn't achieved, mark as achieved
        task.save()
    return redirect("/")

def deleteTask(request,pk):
    models.Task.objects.get(pk=pk).delete()
    return redirect("/")
