from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('discussions/', views.get_discussion_list, name='discussions'),
    path('discussion/<slug:slug>/', views.get_discussion_page, name='discussion'),
    path('delete-comment/<int:id>', views.delete_comment, name='delete_comment'),

    path('add-discussion/', views.add_discussion, name='add_discussion'),
    path('discussion/<slug:slug>/add-discussion-task', views.add_discussion_task, name='add_discussion_task'),
    path('update-discussion/<slug:slug>', login_required(views.DiscussionUpdateView.as_view()), name='update_discussion'),
    path('delete-discussion/<slug:slug>/', views.delete_discussion, name='delete_discussion'),

    path('search/', views.search, name='search'),
]