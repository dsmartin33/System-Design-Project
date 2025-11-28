from django.db import models


class Training(models.Model):
    TrainingID = models.AutoField(primary_key=True)
    TrainingCourseName = models.CharField(max_length=75, null=True)
    Description = models.CharField(max_length=150, null=True, blank=True)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Training'
        unique_together = ('TrainingID', 'TrainingCourseName')

    def __str__(self):
        return f"{self.TrainingID} {self.TrainingCourseName} {self.StartDate} {self.EndDate}"