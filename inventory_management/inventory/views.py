from rest_framework import viewsets
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.cache import cache


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        item = cache.get(f"inventory_item_{pk}")
        if not item:
            try:
                item = self.get_object()
                cache.set(f"inventory_item_{pk}", item)
            except InventoryItem.DoesNotExist:
                return Response(status=404)
        serializer = self.get_serializer(item)
        return Response(serializer.data)
