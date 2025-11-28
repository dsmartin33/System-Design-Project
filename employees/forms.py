from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['EmpID', 'FirstName', 'LastName', 'BirthDate', 'Gender', 'JobTitle', 'Salary', 'HireDate', 'ManagerID']

        widgets = {
            'BirthDate': forms.DateInput(attrs={'type': 'date'}),
            'HireDate': forms.DateInput(attrs={'type': 'date'}),
        }