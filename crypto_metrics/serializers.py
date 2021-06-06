from rest_framework import serializers

from crypto_metrics.models import AlphaVantage


class QoutesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlphaVantage
        fields = '__all__'
