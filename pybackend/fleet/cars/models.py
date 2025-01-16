from django.db import models
from fleet.models import Inventory

class Fleet(models.Model):
    inv_id = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='inventory')
    year = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    seater = models.IntegerField(null=False)
    car_type = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=50, null=False)
    transmission = models.CharField(max_length=50, null=False)
    fuel_type = models.CharField(max_length=50, null=False)
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('out_of_order', 'Out of Order'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    details = models.JSONField(null=False)

    def __str__(self):
        return f"{self.inv_id.car_name} ({self.year}) - {self.status}"