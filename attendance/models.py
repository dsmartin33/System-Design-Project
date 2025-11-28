from django.db import models
from employees.models import Employee
import uuid


def generate_employee_id():
    return f"Temp-{uuid.uuid4().hex[:8]}"


class Attendance(models.Model):
    EmpID = models.OneToOneField(Employee, on_delete=models.CASCADE, default=generate_employee_id, db_column='EmpID', primary_key=True, related_name='attendance_records')
    Date = models.DateField(blank=True, null=True)
    TimeIn = models.CharField(max_length=6, null=True, blank=True)
    TimeOut = models.CharField(max_length=6, null=True, blank=True)

    class Meta:
        db_table = 'Attendance'
        unique_together = ('EmpID', 'Date')

    def __str__(self):
        return f"{self.EmpID.FirstName} {self.EmpID.LastName} {self.Date} {self.TimeIn} {self.TimeOut}"