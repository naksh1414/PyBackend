from django.db import models
from fleet.models import Inventory, Fleet
from users.models import User


class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', null=False)
    fleet_id = models.ForeignKey(Fleet, on_delete=models.CASCADE, related_name='bookings', null=False)
    TYPE_CHOICES = [
        ('chauffeur', 'Chauffeur'),
        ('self', 'Self'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, null=False)
    booking_time = models.DateTimeField(null=False)
    pickup_time = models.DateTimeField(null=False)
    drop_time = models.DateTimeField(null=False)
    total_price = models.IntegerField(null=False)

    # payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='bookings')
    # PAYMENT_STATUS_CHOICES = [
    #     ('pending', 'Pending'),
    #     ('completed', 'Completed'),
    #     ('failed', 'Failed'),
    # ]
    # payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, null=False)

    def __str__(self):
        return f"Booking {self.id} by User {self.user_id.name} for Fleet {self.fleet_id.inv_id.car_name}"
