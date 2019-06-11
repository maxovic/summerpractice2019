from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList, Task

# Create your views here.


def tasks_list(request):
    tasklists = TaskList.objects.all()
    str = ''
    for tasklist in tasklists:
        str += '{}<br>'.format(tasklist.name)
    return HttpResponse(str)


def unique_list(request, id):
    tasklists = TaskList.objects.all()
    return HttpResponse('{}'.format(tasklists[id].name))


def task_in_list(request, id):
    str = '        '
    tasklists = TaskList.objects.all()
    tasklist = tasklists[id]
    tasks = Task.objects.filter(task_list=tasklist)
    for task in tasks:
        str += '{}<br>'.format(task.name)
    return HttpResponse('{}:<br>'.format(tasklist)+str)

def tasks(request, id):
    taskss = Task.objects.all()
    return HttpResponse('<h1> {0} <br> DEADLINE: <br> {1} <br> {2} <br> Status: {3} <h1>'.format(taskss[id].name,taskss[id].created_at, taskss[id].due_on, taskss[id].status))

