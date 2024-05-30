from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('list/', views.get_tasks_list, name='list'),
    path('task-page/<slug:slug>/', views.get_task_page, name='task_page'),
    path('add-task/', views.add_task, name='add_task'),
    path('update-task/<slug:slug>', login_required(views.TaskUpdateView.as_view()), name='update_task'),
    path('delete-task/<slug:slug>/', views.delete_task, name='delete_task'),
    path('toggle-complete/<slug:slug>', views.task_toggle_complete, name='task_toggle_complete'),
    path('add-task/<slug:slug>/add-subtask', views.add_subtask, name='add_subtask'),
    path('update-subtask/<slug:slug>', login_required(views.SubTaskUpdateView.as_view()), name='update_subtask'),
    path('task-page/<slug:slug>/delete-subtask/', views.delete_subtask, name='delete_subtask'),
    path('subtask-toggle-complete/<slug:slug>/', views.subtask_toggle_complete, name='subtask_toggle_complete'),
]