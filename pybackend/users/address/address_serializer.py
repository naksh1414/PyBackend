from rest_framework import serializers
from users.models import Address, User

class AddressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'state', 'country', 'pincode', 'user', 'is_primary']
