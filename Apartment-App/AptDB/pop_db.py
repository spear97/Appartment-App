from initialize import init  # Importing the init function
init()  # Initializing the Django app

from app.models import *  # Importing all models from the app
import pandas as pd  # Importing pandas for data manipulation

# Read the Excel file into a DataFrame
#df = pd.read_excel('ApartmentLIst.xlsx', sheet_name='Data', engine='openpyxl')

# Iterate over each row and convert it to a list of lists
#row_lists = df.values.tolist()

# Clean up data: Remove trailing spaces from string elements
#row_lists = [[value[:-1] if isinstance(value, str) and value.endswith(" ") else value for value in row] for row in row_lists]

# Iterate over each list in row_lists and create model instances
"""
for row in row_lists:

    # Extract data from the row
    apt_name, apt_address, min_amount, max_amount, phone_number, url = row

    # Create Apt instance and save it
    apt_instance = Apt.objects.create(name=apt_name, address=apt_address)

    # Create Amounts instance and save it
    amounts_instance = Amounts.objects.create(minimum=min_amount, maximum=max_amount, apt=apt_instance)

    # Create Info instance and save it
    info_instance = Info.objects.create(phone_number=phone_number, url=url, apt=apt_instance)
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

path = os.path.join(BASE_DIR, 'app', 'templates')

print(path)