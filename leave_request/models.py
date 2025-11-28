import uuid
from django.db import models
from employees.models import Employee


def generate_employee_id():
    return f"Temp-{uuid.uuid4().hex[:8]}"


class LeaveRequest(models.Model):
    STATUS = [('Pending','Pending'), ('Approved','Approved'), ('Rejected','Rejected')]
    LEAVE_TYPE =[('Sick','Sick'), ('Vacation','Vacation'), ('Other','Other')]
    EmpID = models.OneToOneField(Employee, on_delete=models.CASCADE, default=generate_employee_id(), db_column='EmpID', primary_key=True, related_name='leave_requests')
    StartDate = models.DateField(blank=True, null=True)
    EndDate = models.DateField(blank=True, null=True)
    LeaveType = models.CharField(blank=True, null=True, max_length=10, choices=LEAVE_TYPE)
    Status = models.CharField(max_length=20, blank=True, null=True, choices=STATUS, default='pending')

    class Meta:
        db_table = 'LeaveRequest'
        unique_together = ('EmpID', 'LeaveType', 'StartDate', 'EndDate')

    def __str__(self):
        return f"{self.EmpID.FirstName} {self.EmpID.LastName} - {self.LeaveType} ({self.StartDate} to {self.EndDate})"