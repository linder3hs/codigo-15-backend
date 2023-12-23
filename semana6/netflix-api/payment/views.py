from rest_framework.viewsets import ModelViewSet
from .serializers import PaymentSerializer
from .models import Payment
import requests
from decouple import config


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request):
        data = {
            'description': 'Primera venta',
            'installments': request.data.get('installments'),
            'issuer_id': request.data.get('issuer_id'),
            'payer': {
                'email': request.data.get('payer_email'),
            },
            'payment_method_id': request.data.get('payment_method_id'),
            'token': request.data.get('token'),
            'transaction_amount': request.data.get('amount')
        }

        response = requests.post(
            'https://api.mercadopago.com/v1/payments',
            json=data,
            headers={
                'Authorization': f'Bearer {config("MERCADOPAGO_ACCESS_TOKEN")}',
                'Content-Type': 'application/json'
            }
        )

        print("-----------")
        print(response.text)
        print("-----------")
        print(response.json())
        return super().create(request)
