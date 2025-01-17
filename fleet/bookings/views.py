from rest_framework.views import APIView
from .models import Booking, Fleet, User
from .booking_serializer import BookingSerializer

import json
from django.http import JsonResponse
from utils import response_dict
from datetime import datetime


class BookingCreateView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist as e:
            return  JsonResponse(response_dict(code=404, data="user not found"))

        bookings = Booking.objects.filter(user_id=user)
        serialized = BookingSerializer(bookings, many=True)
        return JsonResponse(response_dict(data=serialized.data))

    def post(self, request, user_id):
        body = json.loads(request.body)
        pickup_time = body.get("pickup_time", None)
        drop_time = body.get("drop_time", None)
        if pickup_time:
            pickup_time = datetime.strptime(pickup_time, '%Y-%m-%d %H:%M:%S')
        else:
            return JsonResponse(response_dict(data='provide pickup time', code=400))
        if drop_time:
            drop_time = datetime.strptime(drop_time, '%Y-%m-%d %H:%M:%S')
        else:
            return JsonResponse(response_dict(data='provide drop time', code=400))

        try:
            fleet = Fleet.objects.get(id=body.get("fleet_id"))
        except Fleet.DoesNotExist as e:
            return JsonResponse(response_dict(data="fleet doesn't exist", code=400))

        user = User.objects.get(id=user_id)
        booking = Booking.objects.create(
            user_id=user,
            fleet_id=fleet,
            type=body.get('type'),
            booking_time=datetime.now(),
            pickup_time=pickup_time,
            drop_time=drop_time,
            total_price=fleet.price
        )

        booking_serialized = BookingSerializer(booking)

        return JsonResponse(response_dict(data=booking_serialized.data))
