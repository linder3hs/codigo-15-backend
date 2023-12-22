from django.db import models
from django.contrib.auth.models import User
from subscription.models import Subscription
from django.core.validators import MaxValueValidator


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    subscription = models.OneToOneField(
        Subscription, on_delete=models.CASCADE, null=True)
    payment_day = models.PositiveIntegerField(
        validators=[MaxValueValidator(31)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.first_name

    class Meta:
        db_table = "client"


# un cliente puede tener muchos perfiles
class Profile(models.Model):
    avatar = models.TextField()
    name = models.CharField(max_length=200)
    is_child = models.BooleanField()
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="client")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "profile"
