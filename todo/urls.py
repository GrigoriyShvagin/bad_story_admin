from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('list/', views.get_tasks_list, name='list'),
    path('task-page/<slug:slug>/', views.get_task_page, name='task_page'),

    path('add-task/', views.add_task, name='add_task'),

    path('update-task/<slug:slug>', views.edit_task, name='update_task'),
    path('delete-task/<slug:slug>/', views.delete_task, name='delete_task'),
    path('delete-confirmation/', views.get_delete_confirmation, name='delete_confirmation'),
    path('confirm-delete/<slug:slug>/', views.confirm_delete, name='confirm'),
    path('toggle-complete/<slug:slug>/', views.task_toggle_complete, name='task_toggle_complete'),

    path('add-task/<slug:slug>/add-subtask', views.add_subtask, name='add_subtask'),

    path('update-subtask/<slug:slug>/', login_required(views.SubTaskUpdateView.as_view()), name='update_subtask'),
    path('task-page/<slug:slug>/delete-subtask/', views.delete_subtask, name='delete_subtask'),
    path('subtask-delete-confirmation/', views.get_subtask_delete_confirmation, name='subtask_delete_confirmation'),
    path('confirm-subtask-delete/<slug:slug>/', views.confirm_subtask_delete, name='subtask_confirm'),
    path('subtask-toggle-complete/<slug:slug>/', views.subtask_toggle_complete, name='subtask_toggle_complete'),
]