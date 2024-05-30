from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from uuslug import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Discussions(models.Model):
    class Status(models.IntegerChoices):
        CLOSE = 0, 'Закрыто'
        OPEN = 1, 'Открыто'

    title = models.CharField(max_length=255, verbose_name='Название обсуждения')
    description = models.TextField(blank=True, verbose_name='Описание обсуждения')
    status = models.IntegerField(choices=Status.choices, default=Status.OPEN)
    slug = models.SlugField(max_length=250, unique=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания обсуждения')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления обсуждения')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='discussions', null=True, default=None)

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['time_create'])
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Discussions, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('discussion', args=[self.slug])

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    discussion = models.ForeignKey(Discussions, on_delete=models.CASCADE, related_name='comments')
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    body = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='comments')

    class MPTTMeta:
        order_insertion_by = ['-created']

    def __str__(self):
        try:
            return f'{self.author.username}: {self.body[:30]}'
        except ValueError:
            return f'Нет автора: {self.body[:30]}'