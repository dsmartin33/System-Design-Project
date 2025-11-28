from django.urls import path
from . import views

urlpatterns = [
    path('', views.performance_review_list, name='performance_review_list'),
    path('add/', views.add_performance_review, name='add_performance_review'),
    path('edit/<int:pk>/', views.edit_performance_review, name='edit_performance_review'),
    path('goals/<int:pk>/', views.edit_performance_review_goals, name='edit_performance_review_goals'),
    path('delete/<int:pk>/', views.delete_performance_review, name='delete_performance_review'),
]