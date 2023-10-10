from django.shortcuts import render

def index(request):
    return render(request, 'todo_app/index.html')
