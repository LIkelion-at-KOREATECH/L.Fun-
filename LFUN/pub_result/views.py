from django.shortcuts import render
from place.models import Place
from . import views

# Create your views here.

def pub(request):
    return render(request, 'pub.html')
