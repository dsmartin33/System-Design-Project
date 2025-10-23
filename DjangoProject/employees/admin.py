from django.contrib import admin
from .models import *

models = [Department, Project, Training, Employee, EmployeeProject, EmployeeTraining, Attendance, LeaveRequest, Payroll, PerformanceReview]
for m in models:
    admin.site.register(m)