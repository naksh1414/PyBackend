from django.http import JsonResponse

import json

from users.models import User, Address
from .address_serializer import AddressSerializer

from utils import response_dict
from rest_framework.views import APIView



class Address_view(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist as e:
            return JsonResponse(response_dict(code=404, data="user not found"))

        address = Address.objects.filter(user_id=user_id)
        serialized_data = AddressSerializer(address, many=True)

        return JsonResponse(response_dict(data=serialized_data.data))


    def post(self, request, user_id):
        body = json.loads(request.body)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist as e:
            return JsonResponse(response_dict(code=404, data="user not found"))

        address = Address.objects.create(
            street = body.get("street"),
            city = body.get("city"),
            state = body.get("state"),
            country = body.get("country"),
            pincode = body.get("pincode"),
            is_primary = body.get("isPrimary"),
            user = user
        )

        return JsonResponse(response_dict(data=AddressSerializer(address).data))


    def put(self, request, user_id):
        body = json.loads(request.body)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist as e:
            return JsonResponse(response_dict(code=404, data="user not found"))

        try:
            address = Address.objects.get(id=body.get('id'))
        except Address.DoesNotExist as e:
            return JsonResponse(response_dict(code=404, data="address not found"))

        address.street = body.get('street')
        address.city = body.get('city')
        address.state = body.get('state')
        address.country = body.get('country')
        address.pincode = body.get('pincode')
        address.is_primary = body.get('is_primary')
        address.save()

        return  JsonResponse(response_dict(data=AddressSerializer(address).data))