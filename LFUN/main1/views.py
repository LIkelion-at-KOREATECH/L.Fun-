from django.shortcuts import render, get_object_or_404
from place.models import Place
from mirim.models import Funding
from django.core.paginator import Paginator # 페이지에 출력하는 게시글 수 조절

# Create your views here.
def home1(request):
    places = Place.objects
    place_list = Place.objects.all() # Place의 모든 객채 대상으로
    paginator = Paginator(place_list,4) # Place객체 4개를 한 페이지로 자르기
    page = request.GET.get('page') # reuest된 페이지 알아내서 변수 page에 담음
    posts = paginator.get_page(page) # request 된 페이지 얻어옴
    return render(request, 'home1.html', {'places':places, 'posts':posts})

def home2(request):
    places = Place.objects
    place_list = Place.objects.all() # Place의 모든 객채 대상으로
    paginator = Paginator(place_list,4) # Place객체 4개를 한 페이지로 자르기
    page = request.GET.get('page') # reuest된 페이지 알아내서 변수 page에 담음
    posts = paginator.get_page(page) # request 된 페이지 얻어옴
    return render(request, 'home2.html', {'places':places, 'posts':posts})

def posting1(request, pk):
    places = get_object_or_404(Place, pk=pk)
    return render(request, 'posting1.html', {'places':places})

def posting2(request, pk):
    places = get_object_or_404(Place, pk=pk)
    return render(request, 'posting2.html', {'places':places})
