from rest_framework.routers import DefaultRouter
from .api_views import EmployeeProjectViewSet

router = DefaultRouter()
router.register(r'', EmployeeProjectViewSet, basename='emp_projects')

urlpatterns = router.urls