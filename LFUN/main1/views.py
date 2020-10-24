from django.shortcuts import render, get_object_or_404
from place.models import Place

# Create your views here.
def home1(request):
    places = Place.objects
    return render(request, 'home1.html', {'places':places})

def home2(request):
    places = Place.objects
    return render(request, 'home2.html', {'places':places})

def posting1(request, pk):
    places = get_object_or_404(Place, pk=pk)
    return render(request, 'posting1.html', {'places':places})

def posting2(request, pk):
    places = get_object_or_404(Place, pk=pk)
    return render(request, 'posting2.html', {'places':places})
