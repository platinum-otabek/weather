import json
import os.path
from time import sleep

from celery.schedules import crontab

from app.models.City import City
from app.models.Country import Country
from app.models.Forecast import Forecast
from app.serializers import CitySerializer
from config.celery import app
from config.settings import env
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.task
def update_forecast():
    all_city = City.objects.all()
    serializer = CitySerializer(all_city, many=True)

    for city in serializer.data:
        url = env('URL_WEATHER')
        querystring = {"q": city['name'],
                       "units": "metric",
                       }
        headers = {
            'x-rapidapi-host': env('HEADER_HOST'),
            'x-rapidapi-key': env('HEADER_KEY')
        }
        result = requests.request("GET", url, headers=headers, params=querystring, json={"key": "value"})
        data = result.json()
        Forecast.objects.filter(city__id=city['id']).update(data=data)


@app.task
def search_city_online(city):
    sleep(10)
    url = env('URL_WEATHER')
    querystring = {"q": city,
                   "units": "metric",
                   }
    headers = {
        'x-rapidapi-host': env('HEADER_HOST'),
        'x-rapidapi-key': env('HEADER_KEY')
    }
    result = requests.request("GET", url, headers=headers, params=querystring, json={"key": "value"})
    if result.status_code == 200:
        data = result.json()
        country_code = data['sys']['country']
        try:
            country = Country.objects.get(code=country_code)
        except Country.DoesNotExist:
            country = Country.objects.create(code=country_code)
        city = City.objects.create(
            name=city,
            country=country,
            lat=data['coord']['lat'],
            lang=data['coord']['lon']
        )
        forecast = Forecast.objects.create(
            city=city,
            data=data,
        )
    return data

@app.task
def add_city():
    with open(os.path.join(BASE_DIR,'files/city.list.json'), 'r') as json_file:
        all_cities = json.loads(json_file.read())
        city_limit = os.environ.get('CITY_LIMIT') or 20
    for i in range(0, range(0,city_limit)):
        country_code = all_cities[i]['country']
        try:
            country  = Country.objects.get(code=country_code)
        except Country.DoesNotExist:
            country = Country.objects.create(code=country_code)
        city_name = all_cities[i]['name']
        try:
            city = City.objects.get(name=city_name)
        except City.DoesNotExist:
            City.objects.create(
                name=city_name,
                country=country,
                lat=all_cities[i]['coord']['lat'],
                lang=all_cities[i]['coord']['lon']
            )
    return True


app.conf.beat_schedule = {
    'every 10 min': {
        'task': 'app.tasks.update_forecast',
        'schedule': crontab('*/10')
    }
}
