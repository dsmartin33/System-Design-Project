from django import forms
from .models import PerformanceReview, PerformanceReviewGoals


class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = ['EmpID', 'ManagerID', 'ReviewDate', 'Rating', 'Comments']
        widgets = {
            'ReviewDate': forms.DateInput(attrs={'type': 'date'}),
            'Rating': forms.NumberInput(attrs={'step': '0.1', 'min': '0', 'max': '10'}),
            'Comments': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned = super().clean()
        emp = cleaned.get('EmpID')
        mgr = cleaned.get('ManagerID')

        if emp and mgr and emp == mgr:
            self.add_error('ManagerID', 'Employee cannot be their own manager.')
        return cleaned


class PerformanceReviewGoalsForm(forms.ModelForm):
    class Meta:
        model = PerformanceReviewGoals
        fields = ['PerformanceGoals']
        widgets = {
            'PerformanceGoals': forms.Textarea(attrs={'rows': 4}),
        }