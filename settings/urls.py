from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social.urls')),
    path('todo/', include('todo.urls', namespace='todo')),
    path('links/', include('links.urls', namespace='links')),
    path('cloud/', include('cloud.urls', namespace='cloud')),
    path('calendar/', include('calendars.urls', namespace='calendar')),
    path('users/', include('users.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)