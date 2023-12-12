from rest_framework import serializers

from pricing.models import Prices


class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = '__all__'