from rest_framework.routers import DefaultRouter
from .api_views import AttendanceViewSet

router = DefaultRouter()
router.register(r'', AttendanceViewSet, basename='attendance')

urlpatterns = router.urls