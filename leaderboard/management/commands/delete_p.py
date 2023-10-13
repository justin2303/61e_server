from django.core.management.base import BaseCommand
from leaderboard.models import Player  # Import your model
import os

class Command(BaseCommand):
    help = 'Create user profiles from a text file'

    def handle(self, *args, **options):
        Player.objects.all().delete()
        print("Player database sucessfully resetted")


