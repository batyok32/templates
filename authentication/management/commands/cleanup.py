from django.core.management.base import BaseCommand
from django.conf import settings
import os

# import glob
from pathlib import Path

# calm
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# genre_app = os.path.join(BASE_DIR / "genres/migrations/")
auth_app = os.path.join(BASE_DIR / "authentication/migrations/")
main_app = os.path.join(BASE_DIR / "crude/migrations/")

app_list = [main_app, auth_app]


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        # Greeting
        print(f"{bcolors.BOLD}{bcolors.OKGREEN}\nStarted cleaning...\n{bcolors.ENDC}")

        # Looping in apps
        for app in app_list:

            # Taking only files from directory (not folders)
            onlyfiles = [
                f for f in os.listdir(app) if os.path.isfile(os.path.join(app, f))
            ]

            # If files more than one (__init.py__)
            if len(onlyfiles) > 1:
                print(
                    f"{bcolors.BOLD}{bcolors.WARNING}Deleting in - {bcolors.ENDC} {app} \n"
                )
                # Looping all files
                for clenup in onlyfiles:
                    # Do not delete __init__.py
                    if not clenup.endswith("__init__.py"):
                        print(
                            f"{bcolors.FAIL}{bcolors.BOLD}Deleted - {clenup}{bcolors.ENDC}"
                        )
                        # Delete file
                        os.remove(os.path.join(f"{app}/{clenup}"))
        # Delete db
        db = os.path.join(BASE_DIR / "db.sqlite3")
        if os.path.exists(db):
            os.remove(db)
            print(f"{bcolors.WARNING}{bcolors.BOLD}\nDeleted - Database{bcolors.ENDC}")
        # Ended
        print(f"{bcolors.BOLD}{bcolors.OKGREEN}\nEnded cleaning...\n{bcolors.ENDC}")
