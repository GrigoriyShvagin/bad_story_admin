from django.contrib import admin
from .models import Discussions, Comment
from mptt.admin import MPTTModelAdmin

@admin.register(Discussions)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'time_create', 'time_update']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Comment, MPTTModelAdmin)
# Переписать регистарцию