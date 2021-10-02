from rest_framework import serializers

from app.models.Country import Country


class CountryySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('code',)
