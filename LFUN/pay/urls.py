from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.pay_page, name='pay_page'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)