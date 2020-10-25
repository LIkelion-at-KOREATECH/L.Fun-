from django.shortcuts import render, get_object_or_404

# Create your views here.
def pay_page(request):
    
    return render(request, 'pay.html')