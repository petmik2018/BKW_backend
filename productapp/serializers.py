from rest_framework import serializers

from productapp import models


class ProductProfileSerializer(serializers.ModelSerializer):
    """Serializes a product profile object"""

    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    department_name = serializers.CharField(source='department.name')

    class Meta:
        model = models.Product
        fields = ('id', 'style', 'name', 'color', 'color_name', 'brand_name', 'category_name', 'department_name', 'chapter', 'image_links', 'description', 'get_stock', 'get_images')


class BrandSerializer(serializers.ModelSerializer):
    """"Serializes brand object"""

    class Meta:
        model = models.Brand
        fields = ('id', 'name', 'long_title', 'description', 'link')
