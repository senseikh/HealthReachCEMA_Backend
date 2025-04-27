from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Client
from rest_framework import status

class ClientTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testdoctor', password='testpass123')
        self.client.force_authenticate(user=self.user)
        
        self.client_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'gender': 'M',
            'contact_number': '1234567890',
            'email': 'john.doe@example.com',
            'address': '123 Main St'
        }

    def test_create_client(self):
        response = self.client.post('/api/clients/', self.client_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().first_name, 'John')

    def test_search_client(self):
        Client.objects.create(**self.client_data, created_by=self.user)
        response = self.client.get('/api/clients/?search=John')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)