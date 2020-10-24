from django.shortcuts import render
from place.models import Place
from django.db.models import Q # 검색기능에 사용
from django.core.paginator import Paginator # 페이지에 출력하는 게시글 수 조절에 사용

# Create your views here.

def searchResult1(request): # 비회원용
    places = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        places = Place.objects.all().filter(Q(place_name__contains=query) | Q(place_address__contains=query) |
         Q(place_introduce__contains=query) | Q(place_detailAddress__contains=query) | Q(place_extraAddress__contains=query))
    
    return render(request, 'search1.html', {'query':query, 'places':places})

def searchResult2(request): # 회원용
    # 검색기능
    places = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        places = Place.objects.all().filter(Q(place_name__contains=query) | Q(place_address__contains=query) |
         Q(place_introduce__contains=query) | Q(place_detailAddress__contains=query) | Q(place_extraAddress__contains=query))

    return render(request, 'search2.html', {'query':query, 'places':places})