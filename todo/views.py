from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required

from .models import Task, SubTask
from .forms import AddTaskForm, AddSubTaskForm



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
    request.session['temp'] = {
        'task_slug': task.slug
    }
    return redirect('todo:delete_confirmation')

def get_delete_confirmation(request):
    temp = request.session['temp']
    slug = temp['task_slug']

    return render(request, 'todo/todo-delete-confirmation.html', {'temp': temp, 'slug': slug})


def confirm_delete(request, slug):
    task = get_object_or_404(Task, slug=slug)
    task.delete()
    request.session.pop('temp', None)
    return redirect('todo:list')



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



def edit_task(request, slug):
    task = get_object_or_404(Task, slug=slug)

    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:list')  # или любой другой URL
    else:
        form = AddTaskForm(instance=task)

    value = task.deadline

    return render(request, 'todo/add-task.html', {'form': form, 'value': value})


# class TaskUpdateView(UpdateView):
#     model = Task
#     form_class = AddTaskForm
#     template_name = 'todo/add-task.html'



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
    request.session['temp'] = {
        'subtask_slug': subtask.slug
    }
    return redirect('todo:subtask_delete_confirmation')


def get_subtask_delete_confirmation(request):
    temp = request.session['temp']
    slug = temp['subtask_slug']

    return render(request, 'todo/subtask-delete-confirmation.html', {'temp': temp, 'slug': slug})



def confirm_subtask_delete(request, slug):
    task = get_object_or_404(SubTask, slug=slug)
    task.delete()
    request.session.pop('temp', None)
    return redirect('todo:list')



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

