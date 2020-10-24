from django.shortcuts import render
from place.models import Place
from django.db.models import Q

# Create your views here.

def searchResult1(request): # 비회원용
    places = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        places = Place.objects.all().filter(Q(place_name__contains=query) | Q(place_address__contains=query))
    
    return render(request, 'search1.html', {'query':query, 'places':places})

def searchResult2(request): # 회원용
    places = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        places = Place.objects.all().filter(Q(place_name__contains=query) | Q(place_address__contains=query))
    
    return render(request, 'search2.html', {'query':query, 'places':places})