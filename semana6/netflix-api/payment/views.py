from rest_framework.viewsets import ModelViewSet
from .serializers import PaymentSerializer
from .models import Payment


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
