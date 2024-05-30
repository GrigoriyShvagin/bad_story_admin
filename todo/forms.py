from django import forms
from django.forms import DateInput
from django.db import models

from .models import Task, SubTask


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }


class AddSubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['title', 'description', 'deadline', 'responsible']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }