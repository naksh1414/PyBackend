from django.urls import path


from .views import *


urlpatterns = [
    # path('populate/', populate, name='populate'),
    path('search/', CarSearchView.as_view(), name='Car Search'),
    path('<int:fleet_id>/', get_fleet, name='Get Fleet'),
]
