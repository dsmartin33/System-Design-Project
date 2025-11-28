from django import forms
from .models import EmployeeProject

class EmployeeProjectForm(forms.ModelForm):
    class Meta:
        model = EmployeeProject
        fields = ['EmpID', 'Role', 'HoursWorked', 'ProjectID']