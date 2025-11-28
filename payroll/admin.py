from django.contrib import admin
from .models import Payroll

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('EmpID', 'PayPeriodStart', 'PayPeriodEnd', 'HoursWorked', 'BaseSalary', 'NetPay', 'Deductions', 'DeptID')
    search_fields = ('EmpID__FirstName', 'EmpID__LastName')
    list_filter = ('EmpID', 'PayPeriodStart', 'PayPeriodEnd')