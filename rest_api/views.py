# Implement your views here
from rest_framework import generics, status
from .models import Trade
from .serializers import TradeSerilizer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
 
 
class TradeListCreateView(generics.ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerilizer
    
    def create(self, request, *args, **kwargs):
        shares = request.data.get('shares')
        trade_type = request.data.get('type')
        
        if not (1 <= shares <= 100) or trade_type not in ['buy', 'sell']:
            return Response({"error": "Invalid payload"},status=status.HTTP_400_BAD_REQUEST)
        trade = Trade.objects.create(
            shares=shares, trade_type=trade_type
        )
        serializer = TradeSerilizer(trade)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 
class TradeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerilizer
 