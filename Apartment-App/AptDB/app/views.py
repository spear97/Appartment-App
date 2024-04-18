from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def browse_all(request):
    return render(request, 'browseall.html')

def search_apts(request):
    return render(request, 'index.html')