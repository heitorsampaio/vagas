from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from contracts.serializers import ContractSerializer
from ipware import get_client_ip
from contracts.models import Contract
from contracts.permissions import IsOwner


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def queryset(self):
        return Contract.objects.filter(client=self.request.user)

    def create(self, serializer):
        client_ip = get_client_ip(self.request)
        serializer.save(client=self.request.user, ip_address=client_ip)
