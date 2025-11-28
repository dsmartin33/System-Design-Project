from django.contrib import admin
from .models import EmployeeProject

@admin.register(EmployeeProject)
class EmployeeProjectAdmin(admin.ModelAdmin):
    list_display = ('EmpID', 'Role', 'HoursWorked', 'ProjectID')
    search_fields = ('EmpID__FirstName', 'EmpID__LastName')
    list_filter = ('EmpID', 'Role')