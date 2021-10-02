from django.db import models

from app.models.City import City


class Forecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='forecasts')
    data = models.JSONField(blank=True, null=True, help_text="All data which representing forecast details...")

