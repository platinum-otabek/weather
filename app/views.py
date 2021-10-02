from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.Forecast import Forecast
from app.models.City import City
from app.serializers.forecast import ForecastSerializer
from app.tasks import search_city_online


class GetWeather(APIView):
    def get(self, request):
        search = request.GET.get('search')
        city_queryset = City.objects.filter(name__contains=search)
        forecast_queryset = Forecast.objects.filter(city__id__in=city_queryset)
        serializer = ForecastSerializer(forecast_queryset, many=True)
        if len(serializer.data) == 0:
            search_city_online.delay(search)
            return Response(data={"message": "City not found in our DB"})
        else:
            return Response(data=serializer.data)

