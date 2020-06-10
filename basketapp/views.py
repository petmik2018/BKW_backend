from rest_framework.views import APIView
from rest_framework.response import Response

from basketapp.serializers import BasketSerializer
from basketapp.models import Basket


class BasketView(APIView):
    """Handle getting basket information"""

    def get(self, request, user_pk, format=None):
        basket_items = Basket.objects.filter(user=user_pk)

        serializer = BasketSerializer(basket_items, many=True)

        return Response(serializer.data)
