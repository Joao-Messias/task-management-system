from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import UserRegisterForm  # Import the custom form
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
@login_required(login_url='login')
def home(request):
    form = TaskForm()  # Instancia o formulário para criação da tarefa
    pending_tasks = Task.objects.filter(assigned_to=request.user, status='pending')
    overdue_tasks = Task.objects.filter(assigned_to=request.user, status='overdue')
    completed_tasks = Task.objects.filter(assigned_to=request.user, status='completed')
    return render(request, 'tasks/home.html', {
        'form': form,
        'pending_count': pending_tasks.count(),
        'overdue_count': overdue_tasks.count(),
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
            task.created_by = request.user  # Define o usuário logado como criador da tarefa
            task.save()
            return redirect('home')
    else:
        form = TaskForm()

    # Passando o formulário para o contexto da home
    return render(request, 'tasks/home.html', {
        'form': form,
        'pending_count': Task.objects.filter(status='pending').count(),
        'overdue_count': Task.objects.filter(status='overdue').count(),
        'completed_count': Task.objects.filter(status='completed').count(),
    })

@login_required(login_url='login')
def get_tasks(request, status):
    # Retorna as tarefas do usuário logado com o status especificado
    tasks = Task.objects.filter(assigned_to=request.user, status=status)
    tasks_data = [{'title': task.title, 'description': task.description} for task in tasks]
    return JsonResponse({'tasks': tasks_data})