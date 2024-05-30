from django.contrib import admin
from .models import Folder, File

# Register your models here.
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'file']