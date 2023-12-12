from django.urls import path

from pricing.apps import PricingConfig
from pricing.views import PricesCreateAPIView

app_name=PricingConfig.name

urlpatterns=[
    path('price/create/',PricesCreateAPIView.as_view(),name='price-create'),
]