from rest_framework import status
from rest_framework.test import APITestCase
from .models import Payment
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.test import TestCase


# Create your tests here.
class PaymentTestCase(APITestCase):

    def setUp(self) -> None:
        token = Token.objects.get(user__username="elonmusk")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.valid_payload = {
            "contract": 5,
            "value": 600.0
        }

        self.invalid_payload = {
            "contract": 6,
            "value": 600.0
        }

    def test_create_valid_payment(self) -> None:
        response = self.client.post('/api/payments/',
                                    data=self.valid_payload,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_payment(self) -> None:

        response = self.client.post('/api/payments/',
                                    data=self.invalid_payload,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_payment(self) -> None:
        payment = Payment.objects.filter(
            contract__client__username="elonmusk").first()

        response = self.client.get(self.reverse_url(
            'payments-detail', pk=payment.pk))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_payment_another_client(self) -> None:
        payment = Payment.objects.filter(
            contract__client__username="robertinho").first()

        response = self.client.get(self.reverse_url(
            'payments-detail', pk=payment.pk))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def reverse_url(self, name, **kwargs) -> str:
        url = reverse(name, kwargs=kwargs)
        return url
