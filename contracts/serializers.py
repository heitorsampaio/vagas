from rest_framework import serializers
from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'client_id', 'bank',
                  'amount', 'interest_rate', 'submission_date',
                  'updated_value', 'amount_due', 'ip_address']
        read_only_fields = ['submission_date',
                            'client', 'ip_address', 'balance']
