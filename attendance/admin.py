from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('EmpID', 'Date', 'TimeIn', 'TimeOut')
    search_fields = ('EmpID__FirstName', 'EmpID__LastName')
    list_filter = ('Date',)