from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import InventoryItem


class InventoryItemTests(APITestCase):
    def test_create_item(self):
        url = reverse("inventoryitem-list")
        data = {"name": "Test Item", "description": "Test Description"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_item(self):
        item = InventoryItem.objects.create(
            name="Test Item", description="Test Description"
        )
        url = reverse("inventoryitem-detail", args=[item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests for update and delete...
