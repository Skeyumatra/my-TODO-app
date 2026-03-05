from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=30)  #task name
    isAchieved=models.BooleanField(default=False) 


