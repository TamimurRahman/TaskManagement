from django.shortcuts import render,redirec,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


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

