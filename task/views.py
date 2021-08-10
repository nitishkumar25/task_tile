from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def task_list(request):
    context = {'task_list': Task.objects.all()}
    return render(request, "task/task_list.html",context)


def task_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = TaskForm()
        else:
            task = Task.objects.get(pk=id)
            form = TaskForm(instance=task)
        return render(request, "task/task_form.html", {'form': form})
    else:
        if id == 0:
            form = TaskForm(request.POST)
        else:
            task = Task.objects.get(pk=id)
            form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect ('/task/list')

def task_delete(request,id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('/task/list')
