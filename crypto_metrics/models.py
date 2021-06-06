from django.db import models


class AlphaVantage(models.Model):
    from_currency_code = models.CharField(max_length=100, null=True, blank=True)
    from_currency_name = models.CharField(max_length=100, null=True, blank=True)
    to_currency_code = models.CharField(max_length=100, null=True, blank=True)
    to_currency_name = models.CharField(max_length=100, null=True, blank=True)
    exchange_rate = models.CharField(max_length=100, null=True, blank=True)
    last_refreshed = models.CharField(max_length=100, null=True, blank=True)
    time_zone = models.CharField(max_length=100, null=True, blank=True)
    bid_price = models.CharField(max_length=100, null=True, blank=True)
    ask_price = models.CharField(max_length=100, null=True, blank=True)
