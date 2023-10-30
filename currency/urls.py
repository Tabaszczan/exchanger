from django.urls import path
from .views import CurrencyListAPIView, ExchangeRateAPIView

urlpatterns = [
    path("currency/", CurrencyListAPIView.as_view(), name="currency-list"),
    path(
        "currency/<str:base_currency>/<str:target_currency>/",
        ExchangeRateAPIView.as_view(),
        name="exchange-rate",
    ),
]
