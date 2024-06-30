from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserPasswordChangeForm


def get_login(request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()

    data = {
        'form': form,
    }

    return render(request=request, template_name='users/login.html', context=data)



def get_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))



def get_profile(request):
    user = User.objects.get(username=request.user)
    return render(request=request, template_name='users/profile.html', context={'user': user})


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_form.html'