from django.db import models


class Department(models.Model):
    DeptID = models.AutoField(primary_key=True)
    DeptName = models.CharField(max_length=30, null=True)
    Location = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'Department'
        unique_together = ('DeptID', 'DeptName')

    def __str__(self):
        return f"{self.DeptID} {self.DeptName} {self.Location}"