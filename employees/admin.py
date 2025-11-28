from django.contrib import admin
from employees.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('EmpID', 'FirstName', 'LastName', 'BirthDate', 'Gender', 'HireDate', 'JobTitle', 'Salary', 'ManagerID', 'DeptID')
    search_fields = ('EmpID', 'FirstName', 'LastName', 'BirthDate')
    list_filter = ('LastName',)