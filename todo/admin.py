from django.contrib import admin
from django.forms import DateInput
from .models import Task, SubTask
from django.db import models


@admin.register(Task)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author',  'deadline']
    formfield_overrides = {
            models.DateField: {'widget': DateInput(attrs={'type': 'date'})},
        }

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
