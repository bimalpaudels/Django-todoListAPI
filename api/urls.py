from django.urls import path
from . import views

urlpatterns =[
    path('', views.apiOverview, name='list-urls'),
    path('task-list/', views.taskList, name = 'list-task'),
    path('task-detail/<int:pk>/', views.taskDetail, name='task-detail')
]