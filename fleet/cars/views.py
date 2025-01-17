from django.http import JsonResponse
from rest_framework.views import APIView
from django.db.models import Q

import json
from datetime import datetime

from utils import response_dict

from fleet.models import Fleet, Inventory, Booking
from .fleet_serializer import FleetSerializer
from fleet.inventory.inventory_serializer import InventorySerializer

class CarSearchView(APIView):
    def get(self, request):
        body = json.loads(request.body)
        car_name = body.get('car_name', None)
        fuel_type = body.get('fuel_type', None)
        seater = body.get('seater', None)
        transmission = body.get('transmission', None)
        car_type = body.get('car_type', None)
        pickup_date = body.get('pickup_date')
        drop_date = body.get('drop_date')
        type = body.get('type')

        # Convert pickup and drop date to datetime objects if needed
        pickup_date = datetime.strptime(pickup_date, '%Y-%m-%d %H:%M:%S') if pickup_date else None
        drop_date = datetime.strptime(drop_date, '%Y-%m-%d %H:%M:%S') if drop_date else None

        if type == 'self':
            queryset = Fleet.objects.all()

            # Filter cars based on various search parameters
            if car_name:
                queryset = queryset.filter(inv_id__car_name__icontains=car_name)
            if fuel_type:
                queryset = queryset.filter(fuel_type__icontains=fuel_type)
            if seater:
                queryset = queryset.filter(seater=seater)
            if transmission:
                queryset = queryset.filter(transmission__icontains=transmission)
            if car_type:
                queryset = queryset.filter(car_type__icontains=car_type)

            # Exclude cars that are already booked during the selected time range
            if pickup_date and drop_date:
                booked_fleet_ids = Booking.objects.filter(
                    Q(pickup_time__lt=drop_date, drop_time__gt=pickup_date) |  # Case 1: Full overlap
                    Q(pickup_time__gt=pickup_date, pickup_time__lt=drop_date) |  # Case 2: Pickup within range
                    Q(drop_time__gt=pickup_date, drop_time__lt=drop_date)      # Case 3: Drop within range
                ).values_list('fleet_id', flat=True)

                # Exclude fleet IDs that have bookings during the search time frame
                queryset = queryset.exclude(id__in=booked_fleet_ids)

            fleetSerializer = FleetSerializer(queryset, many=True)
            response = []
            for i in fleetSerializer.data:
                inventory = Inventory.objects.get(id=i['inv_id'])
                car = {
                    'car_name':inventory.car_name,
                    'model':inventory.model,
                    'brand':inventory.brand
                }
                response.append(car | i)

            return JsonResponse(response_dict(data=response))


def get_fleet(request, fleet_id):
    if request.method == 'GET':
        fleet = Fleet.objects.get(id=id)
        fleet_serialized = FleetSerializer(fleet).data
        inventory_data = InventorySerializer(Inventory.objects.get(id=fleet.inv_id)).data
        response = {
            'car_name':inventory_data['car_name'],
            'model':inventory_data['model'],
            'brand':inventory_data['brand']
        }
        return JsonResponse(response_dict(data=response | fleet_serialized))
