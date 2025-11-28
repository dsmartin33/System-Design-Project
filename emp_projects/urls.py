from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_projects_list, name='emp_projects_list'),
    path('add/', views.add_emp_projects, name='add_emp_projects'),
    path('edit/<int:pk_id>/', views.edit_emp_projects, name='edit_emp_projects'),
    path('delete/<int:pk_id>/', views.delete_emp_projects, name='delete_emp_projects'),
]