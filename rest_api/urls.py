from django.urls import path
from .views import TradeListCreateView, TradeRetrieveUpdateDestroyView

urlpatterns = [
    path('trades/', TradeListCreateView.as_view()),
    path('trades/<int:pk>/', TradeRetrieveUpdateDestroyView.as_view()),
]