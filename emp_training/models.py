import uuid
from django.db import models
from employees.models import Employee
from training.models import Training


def generate_employee_id():
    return f"Temp-{uuid.uuid4().hex[:8]}"


class EmployeeTraining(models.Model):
    EmpID = models.OneToOneField(Employee, on_delete=models.CASCADE, default=generate_employee_id, db_column='EmpID', primary_key=True, related_name='employee_trainings')
    TrainingID = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, db_column='TrainingID', related_name='participants')
    CompletionStatus = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'EmployeeTraining'
        unique_together = ('EmpID', 'TrainingID')

    def __str__(self):
        return f"{self.EmpID} {self.TrainingID} {self.CompletionStatus}"