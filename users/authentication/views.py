from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json

from users.models import User

from utils import response_dict


@csrf_exempt
def login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            user = User.objects.get(email=body.get('email'))
            if user.password == body.get('password'):
                return JsonResponse(response_dict(data={
                    "user_id":user.id,
                    "name":user.name,
                    "email":user.email
                }))
            else:
                return JsonResponse(response_dict(code=401, data="Authentication failed"))

        except User.DoesNotExist as e:
            return  JsonResponse(response_dict(code=404, data="user not found"))


@csrf_exempt
def register(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            user = User.objects.get(email=body.get('email'))
            return JsonResponse(response_dict(data="User already exists"))
        except User.DoesNotExist as e:
            user = User.objects.create(
                email=body.get('email'),
                name=body.get('name'),
                mobile=body.get('mobile'),
                password=body.get('password')
            )

        return JsonResponse(response_dict(data={
            'user_id':user.id,
            'name':user.name,
            'email':user.email
        }), status=201)
