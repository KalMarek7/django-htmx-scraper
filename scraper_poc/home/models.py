from django.db import models


# Create your models here.
class ScrapedCurrency(models.Model):
    country = models.CharField(max_length=50)
    currency = models.CharField(max_length=30)
    exchange_rate = models.FloatField()
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.symbol} - {self.currency}"


class LastRefreshDate(models.Model):
    date = models.DateTimeField(auto_now=True)
