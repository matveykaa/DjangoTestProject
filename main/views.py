from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, TaskForDelete

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main page', 'task': tasks})

def aboutus(request):
    return render(request, 'main/aboutus.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Error'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def delete(request):
    error = ''
    if request.method == 'POST':
        form = TaskForDelete(request.POST)
        if form.is_valid():
            title_to_delete = form.cleaned_data['title']
            task = get_object_or_404(Task, title=title_to_delete)
            task.delete()
            return redirect('/')
        else:
            error = 'Error'

    form = TaskForDelete()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/delete.html', context)


def find(request):
    error = ''
    if request.method == 'POST':
        form = TaskForDelete(request.POST)
        if form.is_valid():
            title_to_update = form.cleaned_data['title']
            if title_to_update:
                return redirect('/update', title_to_update)
            else:
                return HttpResponse("<p>Not found</p>")
        else:
            error = 'Error'

    form = TaskForDelete()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/find.html', context)

def update(request, title_to_update):
    task = get_object_or_404(Task, title=title_to_update)
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = TaskForm(instance=task)
    context = {
        'form': form,
        'task': task
    }
    return render(request, 'main/index.html', context)
