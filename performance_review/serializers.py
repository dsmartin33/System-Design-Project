from rest_framework import serializers
from .models import PerformanceReview, PerformanceReviewGoals


class PerformanceReviewGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReviewGoals
        fields = ['PerformanceReviewID', 'PerformanceGoals']


class PerformanceReviewSerializer(serializers.ModelSerializer):
    Goals = PerformanceReviewGoalsSerializer(many=True, read_only=True)

    class Meta:
        model = PerformanceReview
        fields = [
            'PerformanceReviewID',
            'Goals',
            'ReviewDate',
            'Rating',
            'Comments',
            'EmpID',
            'ManagerID'
        ]