from django.contrib import admin

from .models import LastRefreshDate, ScrapedCurrency

# Register your models here.


class ScrapedCurrencyAdmin(admin.ModelAdmin):
    list_display = ["symbol", "country", "exchange_rate", "currency"]
    search_fields = ["symbol", "country", "exchange_rate", "currency"]


admin.site.register(ScrapedCurrency, ScrapedCurrencyAdmin)
admin.site.register(LastRefreshDate)
