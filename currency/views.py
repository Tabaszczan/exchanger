from rest_framework.response import Response
from rest_framework import generics, status
from .models import Currency, ExchangeRate
from .serializers import CurrencySerializer, ExchangeRateSerializer
from rest_framework.views import APIView


class CurrencyListAPIView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ExchangeRateAPIView(APIView):
    def get(self, request, base_currency, target_currency):
        try:
            obj = ExchangeRate.objects.get(
                base_currency__code=base_currency, target_currency__code=target_currency
            )
            serializer = ExchangeRateSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ExchangeRate.DoesNotExist:
            return Response(
                {"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND
            )
