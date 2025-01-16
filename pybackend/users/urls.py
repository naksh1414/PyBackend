from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('address/<int:user_id>', Address_view.as_view(), name='address'),
]