from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


class Folder(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название папки')
    slug = models.SlugField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None)
    is_selected = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Folder, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class File(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название файла')
    file = models.FileField(upload_to='files/')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации файла')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name='Папка')

    class Meta:
        ordering = ['-time_create']

    def __str__(self):
        return self.name