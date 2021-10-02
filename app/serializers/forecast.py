from rest_framework import serializers

from app.models.Forecast import Forecast
from app.serializers.city import CitySerializer


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ('city', 'data',)
        # exclude = ('created_time', 'last_updated_time')
