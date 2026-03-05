from django.urls import path
from . import views
urlpatterns = [
    path("",views.homePage,name="home"),
    path("addTask/",views.AddTask,name="addTask"),
    path("editTask/<str:pk>/",views.editTaskName,name="editTask"),
    path("achieveTask/<str:pk>/",views.achieveTask,name="achieveTask"),
    path("deleteTask/<str:pk>/",views.deleteTask,name="deleteTask")
]