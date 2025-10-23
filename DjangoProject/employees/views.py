from rest_framework import viewsets, filters
from .models import Employee
from .serializers import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee_list.html", {"employees": employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

@login_required
def delete_employee(request, emp_id):
    emp = get_object_or_404(Employee, EmpID=emp_id)
    emp.delete()
    messages.warning(request, f"Employee {emp.FirstName} {emp.LastName} removed.")
    return redirect("employee_list")

def edit_employee(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['DeptID','DeptName']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('departments').all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['EmpID','FirstName','LastName', 'JobTitle','DeptID']

class EmployeeProjectViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProject.objects.all()
    serializer_class = EmployeeProjectSerializer

class EmployeeTrainingViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTraining.objects.all()
    serializer_class = EmployeeTrainingSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related('employee').all()
    serializer_class = AttendanceSerializer

class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.select_related('employee').all()
    serializer_class = LeaveRequestSerializer

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.select_related('employee').all()
    serializer_class = PayrollSerializer

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.select_related('employee').all()
    serializer_class = PerformanceReviewSerializer
