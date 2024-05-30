from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required

from social.views import menu

from .models import Task, SubTask
from .forms import AddTaskForm, AddSubTaskForm
# Решить вопрос с меню

@login_required()
def get_tasks_list(request):

    tasks = Task.objects.all()

    data = {
        'tasks': tasks,
    }

    return render(request=request, template_name='todo/todo-list.html', context=data)


@login_required()
def get_task_page(request, slug):

    task = get_object_or_404(Task, slug=slug)
    subtasks = task.subtasks.all()
    form = AddTaskForm()

    data = {
        'task': task,
        'subtasks': subtasks,
        'form': form,
    }

    return render(request=request, template_name='todo/task-page.html', context=data)


@login_required()
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.save()
            return HttpResponseRedirect(reverse('todo:list'))
    else:
        form = AddTaskForm()

    data = {
        'form': form,
    }

    return render(request=request, template_name='todo/add-task.html', context=data)


@login_required()
def delete_task(request, slug):
    task = get_object_or_404(Task, slug=slug)
    task.delete()
    return HttpResponseRedirect(reverse('todo:list'))


@login_required()
def task_toggle_complete(request, slug):
    task = get_object_or_404(Task, slug=slug)

    if task.status == 0:
        task.status = 1
        task.save()

    elif task.status == 1:
        task.status = 0
        task.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class TaskUpdateView(UpdateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'todo/add-task.html'


@login_required()
def add_subtask(request, slug):
    task = get_object_or_404(Task, slug=slug)

    if request.method == 'POST':
        form = AddSubTaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.save()
            return redirect('todo:task_page', slug=slug)
    else:
        form = AddSubTaskForm()

        data = {
            'form': form,
        }

        return render(request=request, template_name='todo/add-subtask.html', context=data)


@login_required()
def delete_subtask(request, slug):
    subtask = get_object_or_404(SubTask, slug=slug)
    subtask.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def subtask_toggle_complete(request, slug):
    subtask = get_object_or_404(SubTask, slug=slug)

    if subtask.status == 0:
        subtask.status = 1
        subtask.save()

    elif subtask.status == 1:
        subtask.status = 0
        subtask.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = AddSubTaskForm
    template_name = 'todo/add-subtask.html'