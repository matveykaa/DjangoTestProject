from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    if request.method == 'POST':
        title_to_search = request.POST.get('title')
        tasks = Task.objects.filter(title__icontains=title_to_search)
        return render(request, 'main/index.html', {'title': 'Main page', 'task': tasks, 'query': title_to_search})
    else:
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

def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main page', 'task': tasks})


def update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)
    context = {
        'form': form,
        'task': task
    }
    return render(request, 'main/update.html', context)
