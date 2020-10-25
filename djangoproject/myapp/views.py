from django.shortcuts import render
from .models import Place
# Create your views here.

def home(request):
    places = Place.objects #쿼리셋 
    return render(request,'home.html',{'places':places})

def enlarge(request):
    return render(request,'enlarge.html')

def date(request):
    return render(request,'date.html')
    #쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드


