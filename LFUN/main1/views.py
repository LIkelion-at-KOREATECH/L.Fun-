from django.shortcuts import render
from place.models import Place

# Create your views here.
def home1(request):
    posts = Place.objects
    return render(request, 'home1.html', {'posts':posts})

def home2(request):
    posts = Place.objects,
    return render(request, 'home2.html', {'posts':posts})

def posting1(request):
    posts = Place.objects
    return render(request, 'posting1.html', {'posts':posts})

def posting2(request):
    posts = Place.objects
    return render(request, 'posting2.html', {'posts':posts})