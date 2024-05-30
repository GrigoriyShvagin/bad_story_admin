from django.urls import path
from . import views

app_name = 'cloud'

urlpatterns = [
    path('list/', views.get_cloud_list, name='cloud_list'),
    path('add-folder/', views.create_folder, name='add_folder'),
    path('folder-detail/<slug:slug>/', views.get_folder_detail, name='folder_detail'),
    path('delete-folders/', views.delete_selected_folders, name='delete_folders'),

    path('folder-detail/<slug:slug>/add-file/', views.add_file, name='add_file'),
    path('delete-files/<int:id>', views.delete_file, name='delete_file'),
]