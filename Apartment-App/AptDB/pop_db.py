from initialize import init  # Importing the init function
init()  # Initializing the Django app

from app.models import *  # Importing all models from the app
import pandas as pd  # Importing pandas for data manipulation

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

# Check if the script is being run directly
if __name__ == '__main__':
    # If the script is being run directly, load data from 'ApartmentList.xlsx'
    load_db('ApartmentList.xlsx')  # Assuming load_db is a function defined elsewhere
