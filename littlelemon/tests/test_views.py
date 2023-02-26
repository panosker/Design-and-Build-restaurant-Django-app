from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client=APIClient()
        self.menu_items = [
            Menu.objects.create(title="CoceZero", price=10, inventory = 30),
            Menu.objects.create(title="sprite", price=20, inventory = 10),
            Menu.objects.create(title="water", price=30 , inventory = 40),
        ]

    def test_getall(self):
        response = self.client.get('/api/menu/')
        expected_data = MenuSerializer(self.menu_items, many = True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data , expected_data)