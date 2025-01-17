from .cars.views import *
from .bookings.views import *


# from django.db.models.expressions import field_types
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse

# import json
# import pandas as pd
# import os

# from .models import Fleet, Inventory

# from utils import response_dict

# @csrf_exempt
# def populate(request):
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, 'CARS.xlsx')
#     df = pd.read_excel(file_path, engine='openpyxl')
#     grouped = df.groupby('Car Name')
#     car = {}
#     inv = {}
#     for car_name, group in grouped:
#         car[car_name] = []
#         for index, row in group.iterrows():
#             car[car_name].append({})
#             for col in group.columns:
#                 if col != 'Sr. No':
#                     car[car_name][-1][col] = row[col]

#     for i in car.keys():
#         inv = Inventory.objects.create(
#             car_name=i,
#             model=car[i][0]['Model'],
#             brand=car[i][0]['Brand'],
#             total_count=len(car[i]),
#             available=len(car[i]),
#             colors=[],
#             transmission=[],
#             fuel_type=[]
#         )
#         for j in car[i]:
#             car_ = Fleet.objects.create(
#                 inv_id=inv,
#                 year=j['Year'],
#                 price=j['Price'],
#                 seater=j['Seater'],
#                 car_type=j['Car Type'],
#                 color=j['Colour'],
#                 transmission=j['Transmission'],
#                 fuel_type=j['Fuel Type'],
#                 details={
#                     'Pickup Location': j['Location Pickup'],
#                     'Drop Location': j['Location Drop']
#                 }
#             )
#             if car_.color not in inv.colors:
#                 inv.colors.append(car_.color)
#             if car_.transmission not in inv.transmission:
#                 inv.transmission.append(car_.transmission)
#             if car_.fuel_type not in inv.fuel_type:
#                 inv.fuel_type.append(car_.fuel_type)
#             inv.save()
#     return JsonResponse(response_dict(data='Populated'))
