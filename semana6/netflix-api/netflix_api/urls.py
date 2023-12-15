from django.contrib import admin
from django.urls import path, include
from subscription.views import SubscriptionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'subscription', SubscriptionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
