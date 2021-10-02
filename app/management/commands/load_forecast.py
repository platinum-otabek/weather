from django.core.management.base import BaseCommand

from app.tasks import update_forecast


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        update_forecast()