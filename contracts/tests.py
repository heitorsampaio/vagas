from rest_framework import status
from rest_framework.test import APITestCase
from contracts.models import Contract
from rest_framework.authtoken.models import Token
from django.urls import reverse


class ContractTestCase(APITestCase):
    """
    Classe para testar os contratos
    """

    def setUp(self):
        token = Token.objects.get(user__username='elonmusk')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.payload = {
            'value': '1000.00',
            'interest_rate': '0.010',
            'bank': 'Bank of America'
        }

    def test_create_contract(self):
        re = self.client.post('/api/contracts/',
                              data=self.payload,
                              format='json')

        self.assertEqual(re.status_code, status.HTTP_201_CREATED)

    def test_contract_retrieve(self):
        contract = Contract.objects.filter(client__username='elonmusk').first()
        re = self.client.get(self.reverse_url(
            'contract-detail', pk=contract.pk))

        self.assertEqual(re.status_code, status.HTTP_200_OK)

    def test_contract_update(self):
        contract = Contract.objects.filter(client__username='elonmusk').first()
        re = self.client.put(self.reverse_url(
            'contracts-detail', pk=contract.pk), data={'bank': 'Nubank'}, format='json')

        self.assertEqual(re.status_code, status.HTTP_200_OK)

    def test_non_existent_contract(self):
        contract = Contract.objects.filter(
            client__username='robertinho').first()
        response = self.client.get(
            self.reverse_url('loans-detail', pk=contract.pk))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def reverse_url(self, name, **kwargs):
        url = reverse(name, kwargs=kwargs)
        return url
