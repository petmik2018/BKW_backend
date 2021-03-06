from rest_framework import serializers

from stockapp import models

class StockSerializer(serializers.ModelSerializer):
    """"Serializes stock object"""

    class Meta:
        model = models.Stock
        fields = ('id', 'user', 'product', 'size', 'quantity', 'price')

