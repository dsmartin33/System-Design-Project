import uuid
from django.db import models

def generate_employee_id():
    return f"Temp-{uuid.uuid4().hex[:8]}"


class Department(models.Model):
    DeptID = models.AutoField(primary_key=True)
    DeptName = models.CharField(max_length=30, null=True)
    Location = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'Department'
        unique_together = ('DeptID', 'DeptName')

    def __str__(self):
        return f"{self.DeptID} {self.DeptName} {self.Location}"


class DepartmentLocation(models.Model):
    DeptID = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, db_column='DeptID', related_name='Locations')
    Location = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'DepartmentLocation'

    def __str__(self):
        return f"{self.DeptID} {self.Location}"


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


class Training(models.Model):
    TrainingID = models.AutoField(primary_key=True)
    TrainingCourseName = models.CharField(max_length=30, null=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Training'
        unique_together = ('TrainingID', 'TrainingCourseName')

    def __str__(self):
        return f"{self.TrainingID} {self.TrainingCourseName} {self.StartDate} {self.EndDate}"


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


class EmployeeProject(models.Model):
    EmpID = models.AutoField(primary_key=True)
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, db_column='ProjectID', related_name='project_employees')
    Role = models.CharField(max_length=20, null=True, blank=True)
    HoursWorked = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'EmployeeProject'
        unique_together = ('EmpID', 'ProjectID')

    def __str__(self):
        return f"{self.EmpID} {self.Role} {self.ProjectID}"


class EmployeeTraining(models.Model):
    EmpID = models.AutoField(primary_key=True)
    TrainingID = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, db_column='TrainingID', related_name='participants')
    CompletionStatus = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        db_table = 'EmployeeTraining'
        unique_together = ('EmpID', 'TrainingID')

    def __str__(self):
        return f"{self.EmpID} {self.TrainingID} {self.CompletionStatus}"


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


class LeaveRequest(models.Model):
    STATUS = [('pending','Pending'), ('approved','Approved'), ('rejected','Rejected')]
    LEAVE_TYPE =[('sick','Sick'), ('vacation','Vacation'), ('other','Other')]
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
    PerformanceReviewID = models.ForeignKey(PerformanceReview, on_delete=models.CASCADE, null=True, db_column='PerformanceReviewID', related_name='goals')
    PerformanceGoals = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'PerformanceReviewGoals'

    def __str__(self):
        return f"{self.PerformanceReviewID} - {self.PerformanceGoals}"