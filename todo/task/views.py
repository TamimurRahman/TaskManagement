from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm,login


# Create your views here.

def task_list(request):
    status_filter = request.GET.get('status','all')
    category_filter = request.GET.get('category','all')
    task = Task.objects.filter(user=request.user)
    if status_filter !='all':
        tasks = tasks.filter(is_compleated=(status_filter == 'compleated'))
    if category_filter !='all':
        tasks = tasks.filter(category=category_filter)
    
    compleated_tasks = tasks.filter(is_compleated = True)
    pending_tasks = tasks.filter(is_compleated = False)

    return render(request,'',{
        'status_filter':status_filter,
        'category_filter':category_filter,
        'compleated_tasks':compleated_tasks,
        'pending_tasks':pending_tasks,
    })

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('')
    else:
        form = TaskForm()
    return render(request,'',{'form':form})

def task_detail(request,task_id):
    task = get_object_or_404(Task, id = task_id, user=request.user)
    return render(request,'',{'task':task})

def task_delete(request,task_id):
    task = get_object_or_404(Task,id = task_id,user=request.user)
    task.delete()
    return redirect('')

def task_mark_compleated(request,task_id):
    task = get_object_or_404(Task,id = task_id,user=request.user)
    task.is_compleated =True
    task.save()
    return redirect('')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request,'',{'form':form})


