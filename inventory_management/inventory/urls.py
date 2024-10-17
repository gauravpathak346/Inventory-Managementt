from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"items", InventoryItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
