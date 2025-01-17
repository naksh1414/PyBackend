from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'car_name', 'model', 'brand', 'total_count', 'available', 'colors', 'transmission', 'fuel_type']
