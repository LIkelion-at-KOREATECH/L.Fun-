from django.shortcuts import render

# Create your views here.
def home1(request):
    return render(request, 'home1.html')

def home2(request):
    return render(request, 'home2.html')

def posting1(request):
    return render(request, 'posting1.html')

def posting2(request):
    return render(request, 'posting2.html')