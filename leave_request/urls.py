from django.urls import path
from . import views

urlpatterns = [
    path('', views.leave_request_list, name='leave_request_list'),
    path('add/', views.add_leave_request, name='add_leave_request'),
    path('edit/<int:pk>/', views.edit_leave_request, name='edit_leave_request'),
    path('delete/<int:pk>/', views.delete_leave_request, name='delete_leave_request'),
]