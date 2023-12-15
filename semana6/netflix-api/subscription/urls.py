from .views import SubscriptionViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'subscription', SubscriptionViewSet)

urlpatterns = [
    path("", include(router.urls))
]
