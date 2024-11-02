from django.test import TestCase
from restaurant.views import MenuItemView
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.menu_item1 = MenuItem.objects.create(title="Pizza", price=10.99, inventory=100)
        self.menu_item2 = MenuItem.objects.create(title="Burger", price=5.99, inventory=50)
        self.menu_item3 = MenuItem.objects.create(title="Pasta", price=7.99, inventory=75)

    def test_getall(self):
        response = self.client.get(reverse('menuitem-list'))
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)