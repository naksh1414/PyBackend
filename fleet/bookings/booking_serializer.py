from rest_framework import serializers
from .models import Booking
from fleet.models import Fleet
from users.models import User

class BookingSerializer(serializers.ModelSerializer):
    # Optionally, you can add nested serializers if you want to include related models
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    fleet_id = serializers.PrimaryKeyRelatedField(queryset=Fleet.objects.all())

    class Meta:
        model = Booking
        fields = ['id', 'user_id', 'fleet_id', 'type', 'booking_time', 'pickup_time', 'drop_time', 'total_price']
