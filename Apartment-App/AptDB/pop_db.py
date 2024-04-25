from initialize import init  # Importing the init function
init()  # Initializing the Django app

from app.models import *  # Importing all models from the app
import pandas as pd  # Importing pandas for data manipulation
import requests

def load_db(filename):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(filename, sheet_name='Data', engine='openpyxl')

    # Iterate over each row and convert it to a list of lists
    row_lists = df.values.tolist()

    # Clean up data: Remove trailing spaces from string elements
    row_lists = [[value[:-1] if isinstance(value, str) and value.endswith(" ") else value for value in row] for row in row_lists]

    # Iterate over each list in row_lists and create model instances
    for row in row_lists:
        apt_name, apt_address, min_amount, max_amount, phone_number, url, long, lat = row

        # Get or create Apt instance with the given address
        apt_instance, _ = Apt.objects.get_or_create(address=apt_address, defaults={'name': apt_name})

        # Create Amounts instance and save it
        Amounts.objects.create(minimum=min_amount, maximum=max_amount, apt=apt_instance)

        # Create Info instance and save it
        Info.objects.create(phone_number=phone_number, url=url, apt=apt_instance)

        # Create Coords instance and save it
        Coords.objects.create(long=long, lat=lat, apt=apt_instance)

    #print('Data Successfully stored in Database!')

# Define a function to delete data from specified models
def delete_data():

    # List of models from which data will be deleted
    mymodels = [Info, Amounts, Apt]  # Assuming Info, Amounts, and Apt are Django model classes
    
    # Loop through each model
    for m in mymodels:
        # Delete all objects of the current model
        m.objects.all().delete()

def delete_item(item):
    apt_instance = Apt.objects.get(name=item)
    apt_instance.delete()

def create_new_entry(apt_name, apt_address, min_amount, max_amount, phone_number, url, long, lat):
    # Get or create Apt instance with the given address
    apt_instance, _ = Apt.objects.get_or_create(address=apt_address, defaults={'name': apt_name})

    # Create Amounts instance and save it
    Amounts.objects.create(minimum=min_amount, maximum=max_amount, apt=apt_instance)

    # Create Info instance and save it
    Info.objects.create(phone_number=phone_number, url=url, apt=apt_instance)

    # Create Coords instance and save it
    Coords.objects.create(long=long, lat=lat, apt=apt_instance)

# Check if the script is being run directly
if __name__ == '__main__':

    index = -1

    if index == -1:
        coord_instance = Coords.objects.get(apt_id=816)
        coord_instance.long = 32.57229639192025
        coord_instance.save()

    if index == 0:

        # Data for the new apartment entry
        add_data = "Mansfield Webb Rd & E Debbie Ln, Mansfield, TX 76063"
        name_data = "Villaggio"
        min_rent = 1228
        max_rent = 1994
        phone_number_data = "817-839-2874"
        url_data = "https://www.apartments.com/villaggio-mansfield-tx/9khbed7/"
        long_data, lat_data = 32.609837831329955, -97.10944496115424

        # Get or create the Apt instance
        apt_instance, created = Apt.objects.get_or_create(address=add_data, defaults={'name': name_data})

        # Create or update the Amounts instance
        amounts_instance, created = Amounts.objects.update_or_create(apt=apt_instance, defaults={'minimum': min_rent, 'maximum': max_rent})

        # Create or update the Info instance
        info_instance, created = Info.objects.update_or_create(apt=apt_instance, defaults={'phone_number': phone_number_data, 'url': url_data})

        # Create or update the Coords instance
        coords_instance, created = Coords.objects.update_or_create(apt=apt_instance, defaults={'long': long_data, 'lat': lat_data})

    else:
        info_instance = Info.objects.get(apt_id=674)
        info_instance.phone_number = "682-297-6734"
        info_instance.save()

