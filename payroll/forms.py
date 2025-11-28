from django import forms
from .models import Payroll

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['EmpID', 'PayPeriodStart', 'PayPeriodEnd', 'HoursWorked', 'BaseSalary', 'NetPay', 'Deductions', 'DeptID']

        widgets = {
            'PayPeriodStart': forms.DateInput(attrs={'type': 'date'}),
            'PayPeriodEnd': forms.DateInput(attrs={'type': 'date'}),
        }