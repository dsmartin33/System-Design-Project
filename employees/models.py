import uuid
from django.db import models
from departments.models import Department


def generate_employee_id():
    return f"Temp-{uuid.uuid4().hex[:8]}"


class Employee(models.Model):
    EmpID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    BirthDate = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=8, null=True, blank=True)
    HireDate = models.DateField(null=True, blank=True)
    JobTitle = models.CharField(max_length=50, null=True, blank=True)
    Salary = models.CharField(max_length=12, null=True, blank=True)
    DeptID = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, db_column='DeptID', related_name='employees')
    ManagerID = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, db_column='ManagerID', related_name='managers')

    class Meta:
        db_table = 'Employee'
        unique_together = ('EmpID', 'FirstName', 'LastName')

    def __str__(self):
        return f"{self.EmpID} {self.FirstName} {self.LastName} {self.JobTitle}"