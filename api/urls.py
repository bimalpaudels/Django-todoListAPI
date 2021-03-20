from django.urls import path
from . import views

urlpatterns =[
    path('', views.apiOverview, name='list-urls'),
    path('task-list/', views.taskList, name = 'list-task'),
    path('task-detail/<int:pk>/', views.taskDetail, name='task-detail'),
    path('add-task/', views.taskAdd, name='add-task'),
    path('update-task/<int:pk>/', views.updateTask, name='update-task'),
    path('delete-task/<int:pk>/', views.deleteTask, name='delete-task')
]