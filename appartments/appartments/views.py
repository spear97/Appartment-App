from django.shortcuts import render
from django.http import HttpResponse
from .restapi import *

def index(request):
    return render(request, 'index.html')

def browse_all(request):
    return render(request, 'browseall.html')

def search_apts(request):
    if request.method == 'POST':
        # Assuming you want to retrieve the 'Rent' and 'ZipCode' values
        rent = request.POST.get('Rent')
        zip_code = request.POST.get('ZipCode')

        print(rent, zip_code)
        return render(request, 'index.html')
    else:
        # Handle GET request if needed
        return HttpResponse("Method Not Allowed", status=405)