from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(write_only=True, source='departments', queryset=Department.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Employee
        fields = ['EmpID','FirstName', 'LastName', 'JobTitle','HireDate','DeptID']

class EmployeeProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProject
        fields = '__all__'

class EmployeeTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTraining
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'

class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'

class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = '__all__'
