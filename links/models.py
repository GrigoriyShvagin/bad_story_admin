from django.contrib.auth import get_user_model
from django.db import models


class Links(models.Model):
    LINK_CHOICES = (
    ('Google', 'Google'),
    ('Yandex', 'Yandex'),
    ('Dropbox', 'Dropbox'),
    ('GOOGLE_DISK', 'Google Диск'),
    ('YANDEX_DISK', 'Yandex Диск'),
    ('MAIL_CLOUD', 'Облако Mail'),
    ('SBERDISK', 'Сбердиск'),
    ('Telegram', 'Telegram'),
    ('VK', 'VK'),
    )
    title = models.CharField(max_length=255, verbose_name='Название', null=True, default=None)
    link = models.URLField(max_length=255, verbose_name='Ссылка')
    choice = models.CharField(max_length=50, choices=LINK_CHOICES)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='links', null=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания ссылки')

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['time_create'])
        ]
