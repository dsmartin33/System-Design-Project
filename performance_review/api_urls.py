from rest_framework.routers import DefaultRouter
from .api_views import PerformanceReviewViewSet, PerformanceReviewGoalsViewSet

router = DefaultRouter()
router.register(r'', PerformanceReviewViewSet, basename='performance_review')
router.register(r'goals', PerformanceReviewGoalsViewSet, basename='performance_review_goals')

urlpatterns = router.urls