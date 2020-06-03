from rest_framework.views import APIView
from rest_framework.response import Response

from stockapp.serializers import StockSerializer
from stockapp.models import Stock

class StockView(APIView):
    """Handle getting stock information"""

    def get(self, request, product_pk, format=None):
        stock_items = Stock.objects.filter(product=product_pk)

        serializer = StockSerializer(stock_items, many=True)

        return Response(serializer.data)




