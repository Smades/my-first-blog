from django.shortcuts import render
from .models import Task
from django.utils import timezone
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_list(request):
    return render(request, 'firstapp/index.html')

def learnmore(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'firstapp/learnmore.html', {'form': form, 'tasks': tasks})
