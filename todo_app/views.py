from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm

def index(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('home')
    
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'form': form} 
    return render(request, 'todo_app/index.html', context)

def updateTask(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.status = True
    task.save()
    return redirect('home')

def deleteTask(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('home')