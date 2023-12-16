from rest_framework.viewsets import ModelViewSet
from .models import Actor
from .serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]
