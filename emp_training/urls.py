from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_training_list, name='emp_training_list'),
    path('add/', views.add_emp_training, name='add_emp_training'),
    path('edit/<int:emp_training_id>/', views.edit_emp_training, name='edit_emp_training'),
    path('delete/<int:emp_training_id>/', views.delete_emp_training, name='delete_emp_training'),
]