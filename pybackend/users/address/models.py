from django.db import models
from users.models import User


class Address(models.Model):
    street = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)
    pincode = models.IntegerField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', null=False)
    is_primary = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_primary:
            Address.objects.filter(user=self.user, is_primary=True).update(is_primary=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.street
