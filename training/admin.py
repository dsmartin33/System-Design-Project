from django.contrib import admin
from .models import Training

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('TrainingID', 'TrainingCourseName', 'Description', 'StartDate', 'EndDate')
    search_fields = ('TrainingID', 'TrainingCourseName')
    list_filter = ('TrainingID', 'TrainingCourseName')