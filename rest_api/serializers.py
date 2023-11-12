from rest_framework import serializers
from .models import Trade
 
# Implement your serializers here
class TradeSerilizer(serializers.ModelSerializer):
    model = Trade
    fields = '__all__'