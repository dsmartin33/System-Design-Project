from rest_framework.routers import DefaultRouter
from .api_views import EmployeeTrainingViewSet

router = DefaultRouter()
router.register(r'', EmployeeTrainingViewSet, basename='emp_training')

urlpatterns = router.urls