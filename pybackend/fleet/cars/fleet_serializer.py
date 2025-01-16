from rest_framework import serializers
from .models import Fleet

class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = ['id', 'inv_id', 'year', 'price', 'seater', 'car_type', 'color', 'transmission', 'fuel_type', 'status', 'details']
