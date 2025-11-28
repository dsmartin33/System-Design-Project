from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_list, name='training_list'),
    path('add/', views.add_training, name='add_training'),
    path('edit/<int:pk>/', views.edit_training, name='edit_training'),
    path('delete/<int:pk>/', views.delete_training, name='delete_training'),
]