from django.urls import path
from . import views

urlpatterns = [
    path('', views.payroll_list, name='payroll_list'),
    path('add/', views.add_payroll, name='add_payroll'),
    path('edit/<int:payroll_id>/', views.edit_payroll, name='edit_payroll'),
    path('delete/<int:payroll_id>/', views.delete_payroll, name='delete_payroll'),
]