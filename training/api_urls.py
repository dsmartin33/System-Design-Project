from rest_framework.routers import DefaultRouter
from .api_views import TrainingViewSet

router = DefaultRouter()
router.register(r'', TrainingViewSet, basename='training')

urlpatterns = router.urls