from django.contrib import admin
from .models import EmployeeTraining

@admin.register(EmployeeTraining)
class EmployeeTrainingAdmin(admin.ModelAdmin):
    list_display = ('EmpID', 'CompletionStatus', 'TrainingID')
    search_fields = ('EmpID__FirstName', 'EmpID__LastName')
    list_filter = ('EmpID',)