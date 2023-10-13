from django.core.management.base import BaseCommand
from leaderboard.models import Regiments  # Import your model
import os

class Command(BaseCommand):
    help = 'Create user profiles from a text file'
    def add_arguments(self, parser):
        parser.add_argument('my_argument', type=str, help='A string argument')

    def handle(self, *args, **options):
        date = options['my_argument']
        print(f'You provided the argument: {date}')
        to_delete = Regiments.objects.get(date=date)
        to_delete.delete()
        print(f"successfully deleted Regiments data with date {date}")

