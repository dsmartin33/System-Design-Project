from rest_framework import viewsets
from .models import PerformanceReview, PerformanceReviewGoals
from .serializers import PerformanceReviewSerializer, PerformanceReviewGoalsSerializer


class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.select_related('EmpID').prefetch_related('goals')
    serializer_class = PerformanceReviewSerializer


class PerformanceReviewGoalsViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReviewGoals.objects.select_related('PerformanceReviewID')
    serializer_class = PerformanceReviewGoalsSerializer