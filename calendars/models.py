from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    start_time = models.DateTimeField(verbose_name='Начало')
    end_time = models.DateTimeField(verbose_name='Конец')

    @property
    def get_html_url(self):
        url = reverse('calendar:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'