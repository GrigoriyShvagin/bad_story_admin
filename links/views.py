from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .models import Links
from .forms import AddLinks


@login_required()
def get_links_list(request):
    links = Links.objects.all()
    data = {
        'links': links
    }

    return render(request=request, template_name='links/link-list.html', context=data)


@login_required()
def add_link(request):
    if request.method == 'POST':
        form = AddLinks(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.author = request.user
            link.save()
            return redirect('links:link_list')
    else:
        form = AddLinks()

        return render(request=request, template_name='links/add-link.html', context={'form': form})


@login_required()
def delete_link(request, id):
    link = Links.objects.get(id=id)
    link.delete()
    return redirect('links:link_list')