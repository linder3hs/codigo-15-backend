from django.urls import path, include
from .views import PaymentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
