from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['EmpID', 'Date', 'TimeIn', 'TimeOut']

        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date'}),
        }