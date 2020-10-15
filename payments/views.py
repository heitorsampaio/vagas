from payments.models import Payment
from payments.serializers import PaymentSerializer
from rest_framework.viewsets import ModelViewSet


class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        """
        Get queryset
        """

        return Payment.objects.filter(contract__client=self.request.user)
