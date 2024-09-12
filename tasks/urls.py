from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('create-task/', views.create_task, name='create_task'),
    path('tasks/<str:status>/', views.get_tasks, name='get_tasks'),
    path('tasks/all/<str:status>/', views.get_all_tasks, name='get_all_tasks'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
