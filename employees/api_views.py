from rest_framework import viewsets, filters
from employees.models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('departments').all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['EmpID','FirstName','LastName', 'JobTitle','DeptID']