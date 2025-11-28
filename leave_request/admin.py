from django.contrib import admin
from .models import LeaveRequest

@admin.register(LeaveRequest)
class EmployeeTrainingAdmin(admin.ModelAdmin):
    list_display = ('EmpID', 'StartDate', 'EndDate', 'LeaveType', 'Status')
    list_filter = ('EmpID',)
    search_fields = ('EmpID__FirstName', 'EmpID__LastName')