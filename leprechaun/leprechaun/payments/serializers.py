from rest_framework.serializers import PrimaryKeyRelatedField, ModelSerializer

from leprechaun.payments.models import Payment


class PaymentSerializer(ModelSerializer):
    id = PrimaryKeyRelatedField(queryset=Payment.objects.all(), required=False)

    class Meta:
        model = Payment
        exclude = ["created", "modified"]
        read_only_fields = ["id", "title", "colour_hex", "account"]