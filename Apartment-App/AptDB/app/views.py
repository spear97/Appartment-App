import json
from django.shortcuts import render
from .models import *
from .parser import *

def index(request):

    # Retrieve all Coords instances from the database
    all_coords = list(Coords.objects.values_list('long', 'lat'))

    # Retrieve all names from the Apt model
    all_names = list(Apt.objects.values_list('name', flat=True))

    # Retrieve all addresses from Apt model
    all_addresses = list(Apt.objects.values_list('address', flat=True))

    all_cities = get_cities(all_addresses)

    content = {
        'coords': json.dumps(all_coords),
        'names': json.dumps(all_names),
        'address': json.dumps(all_addresses),
        'cities': all_cities,
    }

    return render(request, 'index.html', content)

def browse_all(request):

     # Retrieve all names from the Apt model
    all_names = list(Apt.objects.values_list('name', flat=True))
    
    return render(request, 'browseall.html')

def search_apts(request):
    return render(request, 'index.html')