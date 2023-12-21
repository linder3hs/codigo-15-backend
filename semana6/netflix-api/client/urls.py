from .views import ClientViewSet, ProfileViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
