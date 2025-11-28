import uuid
from django.db import models
from departments.models import Department


def generate_employee_id():
    return f"Temp-{uuid.uuid4().hex[:8]}"


class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=50, null=True)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)
    DeptID = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, db_column='DeptID')

    class Meta:
        db_table = 'Project'
        unique_together = ('ProjectID', 'ProjectName')

    def __str__(self):
        return f"{self.ProjectID} {self.ProjectName} {self.StartDate} {self.EndDate}"