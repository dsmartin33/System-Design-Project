import uuid
from django.db import models
from employees.models import Employee
from projects.models import Project


def generate_employee_id():
    return f"Temp-{uuid.uuid4().hex[:8]}"


class EmployeeProject(models.Model):
    EmpID = models.OneToOneField(Employee, on_delete=models.CASCADE, default=generate_employee_id, db_column='EmpID', primary_key=True, related_name='employee_projects')
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, db_column='ProjectID', related_name='project_employees')
    Role = models.CharField(max_length=20, null=True, blank=True)
    HoursWorked = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'EmployeeProject'
        unique_together = ('EmpID', 'ProjectID')

    def __str__(self):
        return f"{self.EmpID} {self.Role} {self.ProjectID}"