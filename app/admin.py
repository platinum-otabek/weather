from django.contrib import admin

from app.models.City import City
from app.models.Country import Country
from app.models.Forecast import Forecast

# Register your models here.
@admin.register(Country)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'code',)
    search_fields = ('code',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'lat', 'lang')
    search_fields = ('name',)
    ordering = ('country',)
    list_filter = ('country',)

@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'data',)
    search_fields = ('city',)
    list_filter = ('city',)
