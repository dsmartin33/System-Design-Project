import uuid
from django.db import models
from employees.models import Employee


def generate_employee_id():
    return f"Temp-{uuid.uuid4().hex[:8]}"


class PerformanceReview(models.Model):
    PerformanceReviewID = models.AutoField(primary_key=True)
    EmpID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, db_column='EmpID', related_name='reviews')
    ManagerID = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, db_column='ManagerID', related_name='manager_reviews')
    ReviewDate = models.DateField(blank=True, null=True)
    Rating = models.PositiveSmallIntegerField(blank=True, null=True)
    Comments = models.TextField(blank=True, max_length=500)

    class Meta:
        db_table = 'PerformanceReview'
        unique_together = ('EmpID', 'PerformanceReviewID')

    def __str__(self):
        return f"{self.EmpID.FirstName} {self.EmpID.LastName} - {self.ReviewDate} - {self.Rating}"


class PerformanceReviewGoals(models.Model):
    GoalID = models.AutoField(primary_key=True)
    PerformanceReviewID = models.ForeignKey(PerformanceReview, on_delete=models.CASCADE, db_column='PerformanceReviewID', related_name='goals')
    PerformanceGoals = models.TextField(max_length=1024, blank=True, null=True)

    class Meta:
        db_table = 'PerformanceReviewGoals'

    def __str__(self):
        return f"{self.PerformanceReviewID} - {self.PerformanceGoals}"