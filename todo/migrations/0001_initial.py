# Generated by Django 4.2.1 on 2024-05-23 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0002_discussions_social_disc_time_cr_b0540f_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания обсуждения')),
                ('deadline', models.DateTimeField(verbose_name='Дедлайн')),
                ('status', models.IntegerField(choices=[(0, 'Задача закрыта'), (1, 'Задача открыта')], default=1, verbose_name='Статус')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.discussions')),
            ],
            options={
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название подзадачи')),
                ('description', models.TextField(verbose_name='Описание подзадачи')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания обсуждения')),
                ('deadline', models.DateTimeField(verbose_name='Дедлайн')),
                ('status', models.IntegerField(choices=[(0, 'Подзадача закрыта'), (1, 'Подзадача открыта')], default=1, verbose_name='Статус')),
                ('responsible', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtasks', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='todo.task')),
            ],
            options={
                'ordering': ['-time_create'],
            },
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['time_create'], name='todo_task_time_cr_7e71d2_idx'),
        ),
        migrations.AddIndex(
            model_name='subtask',
            index=models.Index(fields=['time_create'], name='todo_subtas_time_cr_a822dd_idx'),
        ),
    ]
