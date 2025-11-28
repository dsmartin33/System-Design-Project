from rest_framework.routers import DefaultRouter
from .api_views import LeaveRequestViewSet

router = DefaultRouter()
router.register(r'', LeaveRequestViewSet, basename='leave_request')

urlpatterns = router.urls