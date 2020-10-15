from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token


# Create your tests here.
class ClientManagerTest(APITestCase):

    def setUp(self) -> None:
        User.objects.create(name="Elon Musk", cpf="11891921444", username="elonmusk", email='elonmusk@onidata.com',
                            password='test1234')
        User.objects.create(name="Post Malone", cpf="03654653723", username="postmalone", email='postmalone@onidata.com',
                            password='test1234')

        token = Token.objects.get(user__username="elonmusk")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.valid_payload = {
            'name': 'Elon Malone',
            'cpf': '02038870004',
            'email': 'elonmalone@onidata.com',
            'username': 'elonmalone',
            'password': 'test1234'
        }

        self.invalid_payload = {
            'name': 'Heitor Sampaio',
            'cpf': '84826349092',
            'username': 'heitorsampaio',
            'password': 'test1234'
        }

    def test_authentication(self):
        response = self.client.post('/api-token-auth/',
                                    data={'username': 'elonmalone',
                                          'password': 'test1234'},
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_authentication(self):
        response = self.client.post('/api-token-auth/',
                                    data={'username': 'elonmalone',
                                          'password': 'test12345'},
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_user(self):
        response = self.client.post('/api/users/',
                                    data=self.valid_payload,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = self.client.post('/api/users/',
                                    data=self.invalid_payload,
                                    format='json')
        self.assertRaises(ValidationError)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
