from django.db import models
 
# Implement your models here
class Trade(models.Model):
    TRADE_TYPES = [('buy', 'buy'), ('sell', 'sell')]
    
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    symbol = models.CharField(max_length=10)
    price = models.FloatField()
    shares = models.FloatField()
    trade_type = models.CharField(max_length=10, choices=TRADE_TYPES)
    time_stamp = models.DateTimeField(auto_now_add=True)