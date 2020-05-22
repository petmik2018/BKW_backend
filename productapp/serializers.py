from rest_framework import serializers

from productapp import models


class ProductProfileSerializer(serializers.ModelSerializer):
    """Serializes a spruduct profile object"""

    class Meta:
        model = models.Product
        fields = ('id', 'style', 'name', 'color', 'color_name', 'brand', 'category', 'department', 'chapter', 'image_link', 'description')