from rest_framework.viewsets import ModelViewSet
from .models import Client, Profile
from .serializers import ClientSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticated]


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]
