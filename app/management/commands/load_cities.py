from django.core.management.base import BaseCommand
from django.utils import timezone

from app.tasks import add_city


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        add_city()