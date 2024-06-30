from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from django.views.generic.edit import UpdateView

from .models import Discussions, Comment
from .forms import AddDiscussionForm, CreateCommentForm

from todo.forms import AddTaskForm

from .services.lates import get_latest


menu = [
    {'title': 'Главная', 'url': 'index'},
    {'title': 'Обсуждения', 'url': 'discussions'},
]

@login_required()
def index(request):

    data = get_latest()

    return render(request=request, template_name='social/index.html', context=data)


@login_required()
def get_discussion_list(request):

    discussions = Discussions.objects.all()
    paginator = Paginator(discussions, 4)
    page_number = request.GET.get('page')
    discussions = paginator.get_page(page_number)

    data = {
        'discussions': discussions,
    }

    return render(request=request, template_name='social/discussions-list.html', context=data)



@login_required()
def get_discussion_page(request, slug):

    discussion = get_object_or_404(Discussions, slug=slug)

    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.discussion = discussion
            comment.save()
            return redirect('discussion', discussion.slug)
    else:
        form = CreateCommentForm()

    data = {
        'discussion': discussion,
        'form': form,
    }

    return render(request=request, template_name='social/discussion-page.html', context=data)


@login_required()
def delete_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def add_discussion(request):
    if request.method == 'POST':
        form = AddDiscussionForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.save()
            return HttpResponseRedirect(reverse('discussions'))
    else:
        form = AddDiscussionForm()
        data = {
            'form': form,
        }

        return render(request=request, template_name='social/add-discussion.html', context=data)


@login_required()
def add_discussion_task(request, slug):
    discussion = get_object_or_404(Discussions, slug=slug)

    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.discussion = discussion
            task.author = request.user
            task.save()
            return redirect('discussion', slug=slug)
    else:
        form = AddTaskForm()

        data = {
            'form': form,
        }

        return render(request=request, template_name='todo/add-task.html', context=data)


@login_required()
def delete_discussion(request, slug):
    discussion = get_object_or_404(Discussions, slug=slug)

    request.session['temp'] = {
        'discussion_slug': discussion.slug
    }

    return redirect('delete_confirmation')


def get_delete_confirmation(request):
    temp = request.session['temp']
    slug = temp['discussion_slug']

    return render(request, 'social/delete-confirmation.html', {'temp': temp, 'slug': slug})


def confirm_delete(request, slug):
    discussion = get_object_or_404(Discussions, slug=slug)
    discussion.delete()
    request.session.pop('temp', None)
    return redirect('index')


@login_required()
def search(request):
    q = request.POST['q']
    discussions = Discussions.objects.filter(title__icontains=q)
    paginator = Paginator(discussions, 4)
    page_number = request.GET.get('page')
    discussions = paginator.get_page(page_number)

    data = {
        'discussions': discussions,
    }

    return render(request, 'social/search-list.html', context=data)


class DiscussionUpdateView(UpdateView):
    model = Discussions
    fields = ['title', 'description', 'status']
    template_name = 'social/add-discussion.html'