from rest_framework import serializers
from .models import Currency, ExchangeRate


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("code",)


class ExchangeRateSerializer(serializers.ModelSerializer):
    base_currency = serializers.StringRelatedField()
    target_currency = serializers.StringRelatedField()

    class Meta:
        model = ExchangeRate
        fields = (
            "base_currency",
            "target_currency",
            "rate",
        )
