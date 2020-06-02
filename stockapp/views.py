from rest_framework.views import APIView
from rest_framework.response import Response

from stockapp.serializers import StockSerializer
from stockapp.models import Stock

class StockView(APIView):
    """Handle getting stock information"""

    def get(self, request, pk, format=None):
        stock_items = Stock.objects.filter(product=pk)

        serializer = StockSerializer(stock_items, many=True)

        return Response(serializer.data)




