from rest_framework import viewsets
from .models import EmployeeProject
from .serializers import EmployeeProjectSerializer

class EmployeeProjectViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProject.objects.all()
    serializer_class = EmployeeProjectSerializer