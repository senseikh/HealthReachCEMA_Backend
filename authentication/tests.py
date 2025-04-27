from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from clients.models import Client
from rest_framework import status

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_data = {
            'username': 'testdoctor',
            'email': 'testdoctor@example.com',
            'password': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'Test',
            'last_name': 'Doctor',
            'role': 'DOCTOR'
        }
        self.client_data = {
            'username': 'testclient',
            'email': 'testclient@example.com',
            'password': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'Test',
            'last_name': 'Client',
            'role': 'CLIENT',
            'date_of_birth': '1990-01-01',
            'gender': 'M',
            'contact_number': '1234567890',
            'address': '123 Main St'
        }

    def test_register_doctor(self):
        response = self.client.post('/api/auth/register/', self.register_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testdoctor')

    def test_register_client(self):
        response = self.client.post('/api/auth/register/', self.client_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().email, 'testclient@example.com')