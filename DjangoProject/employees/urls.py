from rest_framework import routers
from .views import *
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'trainings', TrainingViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'employee-projects', EmployeeProjectViewSet)
router.register(r'employee-trainings', EmployeeTrainingViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'leave-requests', LeaveRequestViewSet)
router.register(r'payrolls', PayrollViewSet)
router.register(r'performance-reviews', PerformanceReviewViewSet)

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/edit/<int:emp_id>/', views.edit_employee, name='edit_employee'),
    path('employees/delete/<int:emp_id>/', views.delete_employee, name='delete_employee'),
]