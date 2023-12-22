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

api_version = "api/v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_version, include('actor.urls')),
    path(api_version, include('subscription.urls')),
    path(api_version, include('content.urls')),
    path(api_version, include('user.urls')),
    path(api_version, include('country.urls')),
    path(api_version, include('client.urls')),
    path(api_version, include('payment.urls')),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc-ui')
]
