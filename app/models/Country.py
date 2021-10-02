from django.db import models


class Country(models.Model):
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.code
