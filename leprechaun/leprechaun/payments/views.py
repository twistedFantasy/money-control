from leprechaun.payments.models import Payment

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class PaymentsViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated] # FIXME: UserPemission

    def get_queryset(self):
        user = self.request.user
        return Payment.objects.all() if user.is_superuser else Payment.objects.filter(user_id=user.id)
