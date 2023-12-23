from django.db import models
from client.models import Client
from django.core.validators import MaxValueValidator


class Payment(models.Model):
    # payment status
    PAYMENT_STATUS = [
        (1, 'CREADO'),
        (2, 'PENDIENTE'),
        (3, 'PAGADO'),
        (4, 'RECHAZADO')
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payer_email = models.EmailField(max_length=250, null=True)
    payer_document_type = models.CharField(max_length=10, blank=True)
    payer_document_number = models.CharField(max_length=50, blank=True)
    installments = models.PositiveIntegerField(validators=[MaxValueValidator(36)], null=True)
    issuer_id = models.CharField(max_length=100, blank=True)
    payment_method_id = models.CharField(max_length=20, blank=True)
    token = models.CharField(max_length=250, blank=True)
    status = models.PositiveIntegerField(choices=PAYMENT_STATUS, default=1)
    amount = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.client.user.email} - {self.payment_date} - {self.status}'

    class Meta:
        db_table = "payments"
