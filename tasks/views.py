from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_POST

from .forms import UserRegisterForm  # Import the custom form
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib import messages

@login_required(login_url='login')
def home(request):
    form = TaskForm()  # Instancia o formulário para criação da tarefa
    pending_tasks = Task.objects.filter(assigned_to=request.user, status='pending')
    in_progress_tasks = Task.objects.filter(assigned_to=request.user, status='in_progress')
    completed_tasks = Task.objects.filter(assigned_to=request.user, status='completed')
    return render(request, 'tasks/home.html', {
        'form': form,
        'pending_count': pending_tasks.count(),
        'in_progress_count': in_progress_tasks.count(),
        'completed_count': completed_tasks.count(),
    })

def register(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona para home se o usuário estiver logado
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # Use the custom form
        if form.is_valid():
            user = form.save(commit=False)  # Don't save to the database yet
            # Save additional fields
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()  # Save to the database
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()  # Use the custom form
    return render(request, 'tasks/register.html', {'form': form})


@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_to = request.user  # Ajuste conforme necessário
            task.created_by = request.user
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('home')  # Ajuste para a URL desejada
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html', {'form': form})

@login_required(login_url='login')
def get_tasks(request, status):
    # Retorna as tarefas do usuário logado com o status especificado
    tasks = Task.objects.filter(assigned_to=request.user, status=status)
    tasks_data = [{'title': task.title, 'description': task.description, 'id':task.id} for task in tasks]
    return JsonResponse({'tasks': tasks_data})

@login_required(login_url='login')
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ajuste para a URL desejada
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

@login_required(login_url='login')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    task.delete()
    return JsonResponse({'status': 'success'})