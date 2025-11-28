from rest_framework import serializers
from .models import EmployeeTraining

class EmployeeTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTraining
        fields = '__all__'