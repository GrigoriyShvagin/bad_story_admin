from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.conf import settings
import os

from .models import File

@receiver(post_delete, sender=File)
def delete_files(sender, instance, **kwargs):
    if hasattr(instance, 'file') and instance.file:
        file_path = os.path.join(settings.MEDIA_ROOT, str(instance.file))
        if os.path.exists(file_path):
            os.remove(file_path)

# Срабатывает сигнал PostDelete после удаления экземпляра класса File
# Проверяет есть ли у этого экземпляра атрибут file, instance это экземпляр модели
# Если есть то собирается его путь в FilePath
# последнее условие проверяет существует ли такой путь, если да то удалеяте файл по этому пути