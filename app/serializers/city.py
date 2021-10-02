from rest_framework import serializers

from app.models.City import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id','name', 'country', 'lat', 'lang',)
