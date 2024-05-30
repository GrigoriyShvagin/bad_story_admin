from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from slugify import slugify

from social.models import Discussions


class Task(models.Model):
    class Status(models.IntegerChoices):
        CLOSE = 0, 'Задача закрыта'
        OPEN = 1, 'Задача открыта'

    title = models.CharField(max_length=255, verbose_name='Название задачи')
    description = models.TextField(verbose_name='Описание задачи')
    slug = models.SlugField(max_length=255, unique=True, null=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='tasks', null=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания обсуждения')
    deadline = models.DateTimeField(verbose_name='Дедлайн')
    status = models.IntegerField(choices=Status.choices, default=Status.OPEN, verbose_name='Статус')
    discussion = models.ForeignKey(Discussions, on_delete=models.CASCADE, related_name='tasks', null=True, default=None, blank=True)

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['time_create'])
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Task, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('todo:task_page', args=[self.slug])


class SubTask(models.Model):
    class Status(models.IntegerChoices):
        CLOSE = 0, 'Подзадача закрыта'
        OPEN = 1, 'Подзадача открыта'

    title = models.CharField(max_length=255, verbose_name='Название подзадачи')
    description = models.TextField(verbose_name='Описание подзадачи')
    slug = models.SlugField(unique=True, editable=False)
    responsible = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='subtasks', null=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания обсуждения')
    deadline = models.DateTimeField(verbose_name='Дедлайн')
    status = models.IntegerField(choices=Status.choices, default=Status.OPEN, verbose_name='Статус')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['time_create'])
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(SubTask, self).save(*args, **kwargs)


    def get_absolute_url(self):
        if self.task:
            return self.task.get_absolute_url()
        return '#none'