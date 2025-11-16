from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

@login_required
def task_list(request):
    status_filter = request.GET.get('status','all')
    category_filter = request.GET.get('category','all')
    tasks = Task.objects.filter(user=request.user)
    if status_filter !='all':
        tasks = tasks.filter(is_compleated=(status_filter == 'compleated'))
    if category_filter !='all':
        tasks = tasks.filter(category=category_filter)
    
    completed_tasks = tasks.filter(is_completed = True)
    pending_tasks = tasks.filter(is_completed = False)

    return render(request,'task_list.html',{
        'status_filter':status_filter,
        'category_filter':category_filter,
        'compleated_tasks':completed_tasks,
        'pending_tasks':pending_tasks,
    })

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,'task_create.html',{'form':form})

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
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('task_list')
            else:
                return render(request,'registration/login.html',{'form':form}) 
    else:  
        form = AuthenticationForm() 
    return render(request,'registration/login.html',{'form':form})

def logout_view(request):
        logout(request)
        # Redirect to a desired page after logout, e.g., the login page or homepage
        return redirect('login') # Assuming 'login' is the name of your login URL pattern

