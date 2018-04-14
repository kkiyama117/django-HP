from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from main import tasks
from .forms import RegisterForm


def index(request):
    context = {
        'user': request.user,
    }
    result = tasks.add.delay(3, 8)
    while not result.ready():
        print('spam')
    print(result.get())
    return render(request, 'main/index.html', context)


@login_required
def user(request):
    context = {
        'user': request.user,
    }
    return render(request, 'main/user.html', context)


def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'main/register.html', context)


@require_POST
def register_save(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('main:index')
    context = {
        'form': form,
    }
    return render(request, 'main/register.html', context)
