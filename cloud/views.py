import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import CreateFolderForm, DeleteFolderForm, AddFile
from .models import Folder, File


@login_required()
def get_cloud_list(request):
    folders = Folder.objects.all()
    return render(request=request, template_name='cloud/cloud-list.html', context={'folders': folders})


@login_required()
def get_folder_detail(request, slug):
    folder = get_object_or_404(Folder, slug=slug)
    return render(request=request, template_name='cloud/folder_detail.html', context={'folder': folder})


@login_required()
def create_folder(request):
    if request.method == 'POST':
        form = CreateFolderForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.save()
            return redirect('cloud:cloud_list')
    else:
        form = CreateFolderForm()

        return render(request=request, template_name='cloud/add-folder.html', context={'form': form})


@login_required()
def delete_selected_folders(request):
    if request.method == 'POST':
        form = DeleteFolderForm(request.POST)
        if form.is_valid():
            delete_folders = form.cleaned_data.get('folders')
            delete_folders.delete()
            messages.success(request, 'Папки успешно удалены')
            return redirect('cloud:cloud_list')
    else:
        form = DeleteFolderForm()

    return render(request=request, template_name='cloud/delete-folder.html', context={'form': form})


@login_required()
def add_file(request, slug):
    folder = get_object_or_404(Folder, slug=slug)

    if request.method == 'POST':
        form = AddFile(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.folder = folder
            file.author = request.user
            file.save()
            return redirect('cloud:folder_detail', slug=slug)
    else:
        form = AddFile()
        return render(request=request, template_name='cloud/add-file.html', context={'form': form})


@login_required()
def delete_file(request, id):
    delete_files = get_object_or_404(File, id=id)
    request.session['temp'] = {
        'delete_files': delete_files.id
    }
    return redirect('cloud:delete_confirmation')


def get_delete_confirmation(request):
    temp = request.session['temp']
    id = temp['delete_files']

    return render(request, 'cloud/delete-confirmation.html', {'temp': temp, 'id': id})


def confirm_delete(request, id):
    file = File.objects.get(id=id)
    file.delete()
    request.session.pop('temp', None)
    return redirect('cloud:cloud_list')