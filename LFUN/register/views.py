from django.shortcuts import render
from .models import Funding


# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        project_name = request.POST.get('project_name', None)
        project_image = request.FILES.get('project_image', None)
        project_introduce = request.POST.get('project_introduce', None)
        project_category = request.POST.get('project_category', None)
        funding_price = request.POST.get('funding_price', None)
        funded_price = request.POST.get('funded_price', None)
        funding_startday = request.POST.get('funding_startday', None)
        funding_starttime = request.POST.get('funding_starttime', None)
        funding_endday = request.POST.get('funding_endday', None)
        funding_endtime = request.POST.get('funding_endtime', None)
        project_ticketprice = request.POST.get('project_ticketprice', None)
        funding_bank = request.POST.get('funding_bank', None)
        funding_account = request.POST.get('funding_account', None)
        
        funding = Funding(project_image=project_image, project_name=project_name, project_introduce=project_introduce, project_category=project_category, funding_price=funding_price, funding_startday=funding_startday, funding_starttime= funding_starttime, funding_endday=funding_endday,  funding_endtime= funding_endtime, project_ticketprice=project_ticketprice, funding_bank=funding_bank,funding_account=funding_account)
        funding.save()

        return render(request, 'register.html')