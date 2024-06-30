from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'cal'

urlpatterns = [
    path('calendar/', login_required(views.CalendarView.as_view()), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
    path('delete-event/<int:id>', views.delete_event, name='delete_event'),
]