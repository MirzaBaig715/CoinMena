from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from alpha_vantage.foreignexchange import ForeignExchange

from crypto_metrics.serializers import QoutesSerializer
from crypto_metrics.utils.common import format_data
from CoinMena import settings

from crypto_metrics.models import AlphaVantage


class QoutesAPIView(GenericAPIView):

    serializer_class = QoutesSerializer
    def get(self, request, *args, **kwargs):
        """
        Get the latest price from db
        """
        obj = AlphaVantage.objects.order_by('-last_refreshed').first()
        serialized_data = self.serializer_class(obj).data
        return Response(serialized_data)

    def post(self, request, *args, **kwargs):
        """
        Get the latest price from AlpaVantage API
        """
        fe = ForeignExchange(key=settings.ALPHA_API_KEY)
        # There is no metadata in this call
        data, _ = fe.get_currency_exchange_rate(from_currency='BTC', to_currency='USD')
        serialized_data = self.serializer_class(format_data(data)).data
        return Response(serialized_data)


