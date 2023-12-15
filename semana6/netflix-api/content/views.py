from .models import Content
from .serializers import ContentSerializer
from rest_framework.viewsets import ModelViewSet


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
