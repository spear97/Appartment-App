import json
from django.core.management.base import BaseCommand
from app.models import Apt, Amounts, Info, Coords, Images
import os

class Command(BaseCommand):
    help = 'Backup SQLite3 data to JSON'

    def handle(self, *args, **options):

        # Query data
        apt_data = list(Apt.objects.values())
        amounts_data = list(Amounts.objects.values())
        info_data = list(Info.objects.values())
        coords_data = list(Coords.objects.values())
        img_data = list(Images.objects.values())

        data_to_backup = {
            'Apt': apt_data,
            'Amounts': amounts_data,
            'Info': info_data,
            'Coords': coords_data,
            'Images': img_data
        }

        # Serialize data to JSON
        json_data = json.dumps(data_to_backup, indent=4)

        # Get the directory path to save the backup file
        backup_dir = os.path.join(os.getcwd(), 'backups')

        # Create the backup directory if it doesn't exist
        os.makedirs(backup_dir, exist_ok=True)

        # Construct the file path for the backup JSON file
        backup_file_path = os.path.join(backup_dir, 'backup.json')

        # Write JSON data to a file
        with open(backup_file_path, 'w') as json_file:
            json_file.write(json_data)

        # Output that Backup of Data 
        self.stdout.write(self.style.SUCCESS("Backup was successfully created!"))
