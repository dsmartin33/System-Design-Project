from django import forms
from employees.models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['DeptID', 'DeptName', 'Location']