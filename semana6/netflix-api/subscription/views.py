from django.http import JsonResponse


def index(request):
    return JsonResponse({
        "ok": True,
        "data": "Hola mundo"
    })
