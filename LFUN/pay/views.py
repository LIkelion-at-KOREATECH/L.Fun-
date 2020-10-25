from django.shortcuts import render, get_object_or_404
from place.models import Place

# Create your views here.
def pay_page(request):
    places = Place.objects
    return render(request, 'pay.html', {'places':places})