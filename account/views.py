from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from account import forms


def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'account/index.html', context)


@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'account/profile.html', context)


def register(request):
    form = forms.RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)


@require_POST
def register_save(request):
    form = forms.RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('account:index')
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)
