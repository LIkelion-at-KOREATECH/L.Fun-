from django.shortcuts import render
from .models import Place


# Create your views here.


def place(request):
    if request.method == "GET":
        return render(request, 'place.html')
    elif request.method == "POST":
        place_image = request.FILES.get('place_image', None)
        place_address = request.POST.get('place_address', None)
        place_postcode = request.POST.get('place_postcode', None)
        place_detailAddress = request.POST.get('place_detailAddress', None)
        place_extraAddress = request.POST.get('place_extraAddress', None)
        place_price = request.POST.get('place_price', None)
        place_name = request.POST.get('place_name', None)
        place_caution = request.POST.get('place_caution', None)
        place_introduce = request.POST.get('place_introduce', None)
        
        place = Place(place_image=place_image, place_address=place_address, place_postcode=place_postcode, place_detailAddress=place_detailAddress, place_extraAddress=place_extraAddress, place_price=place_price, place_name= place_name, place_caution=place_caution,  place_introduce= place_introduce)
        place.save()

        return render(request, 'placefi.html')

def placefi(request):
    return render(request, 'placefi.html')        