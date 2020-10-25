from django.shortcuts import render, get_object_or_404
from place.models import Place
from mirim.models import Funding

# Create your views here.
def pay_page(request, pk):
    pay = get_object_or_404(Funding, pk=pk)
    return render(request, 'pay.html', {'funding':pay})

def pay_complete(request, pk):
    pay = get_object_or_404(Funding, pk=pk)

    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        pay.funded_price = pay.funded_price + int(request.POST.get('price', None))
        pay.save()

        return render(request, 'pay_complete.html', {'funding':pay})