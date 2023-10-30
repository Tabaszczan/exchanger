from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code


class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(
        Currency, related_name="base_currency", on_delete=models.CASCADE
    )
    target_currency = models.ForeignKey(
        Currency, related_name="target_currency", on_delete=models.CASCADE
    )
    rate = models.FloatField(default=0)
