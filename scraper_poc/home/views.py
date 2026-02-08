from django.http import HttpRequest
from django.shortcuts import render

from .models import LastRefreshDate, ScrapedCurrency

# from .web_scraper import get_nbp_data
from .oop_web_scraper import CurrencyScraper

# from django.views.generic import TemplateView

""" class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["currencies"] = ScrapedCurrency.objects.all()
        return context """


def home(request: HttpRequest):
    refresh_date = "Never"
    date_obj = LastRefreshDate.objects.first()
    if date_obj:
        refresh_date = date_obj.date

    # for htmx query
    if request.headers.get("HX-Request"):
        htmx_query = request.GET.get("qhtmx")
        currencies = ScrapedCurrency.objects.filter(country__icontains=htmx_query)
        return render(
            request,
            "home/partial.html",
            context={"currencies": currencies, "date": refresh_date},
        )

    # for django query
    query = request.GET.get("q")
    if query:
        currencies = ScrapedCurrency.objects.filter(country__icontains=query)
    else:
        currencies = ScrapedCurrency.objects.all()

    return render(
        request,
        "home/home.html",
        context={"currencies": currencies, "date": refresh_date},
    )


# for htmx
def update(request):
    scraper = CurrencyScraper("https://www.google.pl/")
    scraper.get_data()
    scraping_result = scraper.insert_data()

    if scraping_result:
        return render(
            request,
            "home/partial.html",
            context={
                "currencies": scraping_result["currencies"],
                "date": scraping_result["refresh_date"].date,
            },
        )

    refresh_date = "Never"
    date_obj = LastRefreshDate.objects.first()
    if date_obj:
        refresh_date = date_obj.date

    return render(
        request,
        "home/partial.html",
        context={
            "error": "error",
            "currencies": ScrapedCurrency.objects.all(),
            "date": refresh_date,
        },
    )
