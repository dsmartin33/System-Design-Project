from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('DeptID', 'DeptName', 'Location')
    search_fields = ('DeptID', 'DeptName', 'Location')
    list_filter = ('Location',)