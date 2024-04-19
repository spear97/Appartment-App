from django.shortcuts import render
from .models import Apt, Amounts, Info

# Create your views here.
def index(request):
    addresses = Apt.objects.values_list('address', flat=True)
    return render(request, 'index.html')

def browse_all(request):
    return render(request, 'browseall.html')

def search_apts(request):
    return render(request, 'index.html')