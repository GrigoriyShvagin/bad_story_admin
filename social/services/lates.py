from social.models import Discussions, Comment
from links.models import Links
from cloud.models import Folder, File
from todo.models import Task


def get_latest():
    discussions = Discussions.objects.all()[:5]
    task = Task.objects.all()[:5]
    links = Links.objects.all()[:5]
    folders = Folder.objects.all()[:5]
    file = File.objects.all()[:5]
    comment = Comment.objects.all()[:5]

    data = {
        'discussions': discussions,
        'task': task,
        'links': links,
        'folders': folders,
        'file': file,
        'comment': comment,
    }

    return data
