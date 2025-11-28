from django import forms
from .models import Training

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['TrainingID', 'TrainingCourseName', 'Description', 'StartDate', 'EndDate']

        widgets = {
            'StartDate': forms.DateInput(attrs={'type': 'date'}),
            'EndDate': forms.DateInput(attrs={'type': 'date'}),
        }