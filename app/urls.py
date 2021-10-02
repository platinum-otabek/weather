from django.urls import path

from app.views import GetWeather

urlpatterns = [
    path('q/', GetWeather.as_view()),
    # path('update_weather/', UpdateWeather.as_view())
]
