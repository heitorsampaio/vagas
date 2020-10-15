from rest_framework import serializers

from payments.models import Payment
from contracts.models import Contract
from contracts.serializers import ContractSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['contract', 'value', 'date']
        extra_kwargs = {
            'date': {'read_only': True}
        }

    def validate_contract(self, value: Contract):
        """
        Validate Contract
        """

        re = self.context.get('request')

        if value.client != re.user:
            raise serializers.ValidationError(
                'You don\'t have permission to access this contract')
        return value
