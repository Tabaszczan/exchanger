from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from currency.serializers import ExchangeRateSerializer
from .models import Currency, ExchangeRate


class CurrencyListAPIViewTest(APITestCase):
    def setUp(self):
        Currency.objects.create(code="USD")
        Currency.objects.create(code="EUR")
        Currency.objects.create(code="GBP")

    def test_currency_list_api_view(self):
        url = reverse("currency-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_currency_list_api_search_filter(self):
        url = reverse("currency-list")
        response = self.client.get(url, {"search": "USD"})  # Searching for 'USD'

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)


class ExchangeRateAPIViewTest(APITestCase):
    def setUp(self):
        self.usd_currency = Currency.objects.create(code="USD")
        self.eur_currency = Currency.objects.create(code="EUR")

        self.exchange_rate = ExchangeRate.objects.create(
            base_currency=self.usd_currency,
            target_currency=self.eur_currency,
            rate=0.85,
        )

    def test_exchange_rate_api_view(self):
        url = reverse("exchange-rate", args=["USD", "EUR"])
        response = self.client.get(url)
        serializer = ExchangeRateSerializer(self.exchange_rate)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_exchange_rate_api_not_found(self):
        url = reverse("exchange-rate", args=["USD", "GBP"])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"message": "Object not found"})
