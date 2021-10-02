from django.db import models

from app.models.Country import Country


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    lat = models.CharField(max_length=15)
    lang = models.CharField(max_length=15)

    def __str__(self):
        return self.name
