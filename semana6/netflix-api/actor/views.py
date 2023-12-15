from rest_framework.viewsets import ModelViewSet
from .models import Actor
from .serializers import ActorSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
