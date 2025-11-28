import uuid
from django.db import models
from employees.models import Employee
from departments.models import Department


def generate_employee_id():
    return f"Temp-{uuid.uuid4().hex[:8]}"


class Payroll(models.Model):
    EmpID = models.OneToOneField(Employee, on_delete=models.CASCADE, default=generate_employee_id(), db_column='EmpID', primary_key=True, related_name='payrolls')
    DeptID = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, db_column='DeptID')
    PayPeriodStart = models.DateField()
    PayPeriodEnd = models.DateField()
    HoursWorked = models.CharField(max_length=10, null=True, blank=True)
    BaseSalary = models.FloatField(null=True, blank=True)
    NetPay = models.DecimalField(max_digits=10, decimal_places=2)
    Deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'Payroll'
        unique_together = ('EmpID', 'PayPeriodStart', 'PayPeriodEnd')

    def __str__(self):
        return f"{self.EmpID.FirstName} {self.EmpID.LastName} - {self.PayPeriodStart} to {self.PayPeriodEnd} - {self.NetPay}"