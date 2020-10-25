from django.shortcuts import render
# from place.models import Place
from mirim.models import Funding
from django.db.models import Q # 검색기능에 사용
from django.core.paginator import Paginator # 페이지에 출력하는 게시글 수 조절에 사용
                                            # 참고사이트 : https://citylock77.tistory.com/44?category=864190

# Create your views here.

def searchResult1(request): # 비회원용
    places = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        places = Funding.objects.all().filter(Q(project_name__contains=query) | Q(project_introduce__contains=query) |
         Q(project_category__contains=query))
    
    return render(request, 'search1.html', {'query':query, 'places':places})

def searchResult2(request): # 회원용
    # 검색기능
    places = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        places = Funding.objects.all().filter(Q(project_name__contains=query) | Q(project_introduce__contains=query) |
         Q(project_category__contains=query))

    return render(request, 'search2.html', {'query':query, 'places':places})