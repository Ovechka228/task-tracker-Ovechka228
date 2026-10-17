from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('new/', views.TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('', views.TaskListView.as_view(), name='task-list'),
]
