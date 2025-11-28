from rest_framework import viewsets
from .models import EmployeeTraining
from .serializers import EmployeeTrainingSerializer

class EmployeeTrainingViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTraining.objects.all()
    serializer_class = EmployeeTrainingSerializer