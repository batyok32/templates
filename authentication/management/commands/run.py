from django.core.management.base import BaseCommand
from django.conf import settings
import os
from pathlib import Path

# calm
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        print(f"{bcolors.BOLD}{bcolors.OKGREEN}\nStarted Migration...\n{bcolors.ENDC}")
        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")

        
   