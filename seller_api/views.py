from rest_framework import viewsets

from seller_api import serializers
from seller_api import models

class SellerProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updatins profiles"""
    serializer_class = serializers.SellerProfileSerializer
    queryset = models.SellerProfile.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name', 'email',)
