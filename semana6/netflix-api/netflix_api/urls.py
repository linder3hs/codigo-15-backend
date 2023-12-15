from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
  openapi.Info(
    title="Netflix api",
    default_version="v1",
    description="API basado en Netflix",
    license=openapi.License(name="MIT")
  ),
  public=True, 
  permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('actor.urls')),
    path('api/v1/', include('subscription.urls')),
    path('api/v1/', include('content.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui')
]
