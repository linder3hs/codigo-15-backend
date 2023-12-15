from .views import ActorViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r'actor', ActorViewSet)

urlpatterns = [
    path("", include(router.urls))
]
