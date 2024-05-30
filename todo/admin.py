from django.contrib import admin
from django.forms import DateInput
from .models import Task, SubTask
from django.db import models


@admin.register(Task)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'time_create', 'deadline']
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
            models.DateField: {'widget': DateInput(attrs={'type': 'date'})},
        }

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
