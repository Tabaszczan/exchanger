import requests
from .models import Currency, ExchangeRate
from django.conf import settings


def fetch_currencies_data():
    key = getattr(settings, "FIXER_API_KEY", None)
    response = requests.get(f"http://data.fixer.io/api/latest?access_key={key}")
    data = response.json()
    populate_database(data)


def populate_database(data):
    # Assuming data is in the format {'base': 'EUR', 'rates': {'USD': 1.12345, 'GBP': 0.87654, ...}}
    base_currency = Currency.objects.get_or_create(code=data["base"])[0]
    for target_currency, rate in data["rates"].items():
        target_currency_obj = Currency.objects.get_or_create(code=target_currency)[0]
        exchange_rate_obj = ExchangeRate.objects.get_or_create(
            base_currency=base_currency, target_currency=target_currency_obj
        )[0]
        exchange_rate_obj.rate = rate
        exchange_rate_obj.save()
