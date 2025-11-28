from django import forms
from .models import EmployeeTraining

class EmployeeTrainingForm(forms.ModelForm):
    class Meta:
        model = EmployeeTraining
        fields = ['EmpID', 'CompletionStatus', 'TrainingID']