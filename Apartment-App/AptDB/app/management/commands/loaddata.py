import json
from django.core.management.base import BaseCommand
from app.models import Apt, Amounts, Info, Coords
import os

class Command(BaseCommand):
    help = 'Backup SQLite3 data to JSON'

    def handle(self, *args, **options):

        # Get the directory path to save the backup file
        backup_dir = os.path.join(os.getcwd(), 'backups')

        # Construct the file path for the backup JSON file
        backup_file_path = os.path.join(backup_dir, 'backup.json')

        if not os.path.exists(backup_file_path):
            self.stdout.write(self.style.ERROR("ERROR! Backup does not exist! Please create backup and try again!"))
            return

        with open(backup_file_path, 'r') as file:
            data = json.load(file)

            apt, amounts, info, coord = data['Apt'], data['Amounts'], data['Info'], data['Coords']

            apt_length, amounts_length, info_length, coord_length = len(apt), len(amounts), len(info), len(coord)

            if apt_length == amounts_length == info_length == coord_length:
                
                for i in range(apt_length):

                    # Create a new Apt instance
                    new_apt = Apt.objects.create(name=apt[i]['name'], address=apt[i]['address'])

                    # Create a new Amounts instance associated with the newly created Apt
                    Amounts.objects.create(minimum=amounts[i]['minimum'], maximum=amounts[i]['maximum'], apt=new_apt)

                    # Create a new Info instance associated with the newly created Apt
                    Info.objects.create(phone_number=info[i]['phone_number'], url=info[i]['url'], apt=new_apt)

                    # Create a new Coords instance associated with the newly created Apt
                    Coords.objects.create(long=coord[i]['long'], lat=coord[i]['lat'], apt=new_apt)


        # Output that Backup of Data 
        self.stdout.write(self.style.SUCCESS("Data was successfully loaded into the DataBase!"))
