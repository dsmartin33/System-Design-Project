from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('ProjectID', 'ProjectName', 'StartDate', 'EndDate', 'DeptID')
    search_fields = ('ProjectID', 'ProjectName')
    list_filter = ('ProjectID', 'ProjectName', 'StartDate', 'EndDate')