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

    # Retrieve all addresses from Apt model
    all_addresses = list(Apt.objects.values_list('address', flat=True))

    # Retrieve all names from the Apt model
    all_names = list(Apt.objects.values_list('name', flat=True))

    # Retrieve all minimums from the Amounts model
    all_mins = list(Amounts.objects.values_list('minimum', flat=True))

    # Retrieve all maximums from the Amounts model
    all_maxs = list(Amounts.objects.values_list('maximum', flat=True))

    # Retrieve all links from the Info model
    all_links = list(Info.objects.values_list('url', flat=True))

    content = {
        'names': json.dumps(all_names),
        'addresses': json.dumps(all_addresses),
        'mins': json.dumps(all_mins),
        'maxs': json.dumps(all_maxs),
        'links': json.dumps(all_links),
    }
    
    return render(request, 'browseall.html', content)

def search_apts(request):
    return render(request, 'index.html')