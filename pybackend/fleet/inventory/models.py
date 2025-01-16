from django.db import models


class Inventory(models.Model):
    car_name = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=True)
    brand = models.CharField(max_length=255, null=False)
    total_count = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    colors = models.JSONField(null=False)
    transmission = models.JSONField(null=False)
    fuel_type = models.JSONField(null=False)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.car_name})"