from django.urls import path
from . import views

app_name = 'links'

urlpatterns = [
    path('list/', views.get_links_list, name='link_list'),
    path('add-link/', views.add_link, name='add_link'),
    path('delete-link/<int:id>', views.delete_link, name='delete_link')
]