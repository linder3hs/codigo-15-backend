from rest_framework.serializers import ModelSerializer
from .models import Subscription


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        # fields = ("id", "title")
        fields = "__all__"
