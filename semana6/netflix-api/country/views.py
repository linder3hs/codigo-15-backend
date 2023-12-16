from django.http import JsonResponse
from .models import Country
import requests


def create_countries(request):
    data = requests.get(
        "https://cuik-projects.github.io/country-list/countries.json")

    json_res = data.json()

    for country in json_res:
        new_country = Country(
            name=country["name"], dial_code=country["dial_code"], code=country["code"], emoji=country["emoji"])
        new_country.save()

    return JsonResponse({
        "message": "create countries"
    })


def delete_countries(request):
    Country.objects.all().delete()
    return JsonResponse({
        "message": "deleted countries"
    })
