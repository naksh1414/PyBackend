from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255, unique=True, null=False)
    name = models.CharField(max_length=255, null=False)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name
