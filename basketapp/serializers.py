from rest_framework import serializers

from basketapp import models

class BasketSerializer(serializers.ModelSerializer):
    """"Serializes basketobject"""

    class Meta:
        model = models.Basket
        fields = ('product', 'name', 'size', 'quantity', 'price')

