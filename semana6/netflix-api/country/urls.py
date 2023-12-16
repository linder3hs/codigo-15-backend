from .views import create_countries, delete_countries
from django.urls import path

urlpatterns = [
    path('country/create', create_countries),
    path('country/delete', delete_countries)
]
