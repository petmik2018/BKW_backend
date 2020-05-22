from rest_framework import viewsets

from productapp import serializers
from productapp import models

class ProductProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updatins product profiles"""
    serializer_class = serializers.ProductProfileSerializer
    queryset = models.Product.objects.all()
