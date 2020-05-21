from rest_framework import serializers

from seller_api import models


class SellerProfileSerializer(serializers.ModelSerializer):
    """Serializes a seller profile object"""

    class Meta:
        model = models.SellerProfile
        fields = ('id', 'user_profile', 'short_name', 'long_name', 'phone')
        # extra_kwargs = {'user_profile': {'read_only': True}}
