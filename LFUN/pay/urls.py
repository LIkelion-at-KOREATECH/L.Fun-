from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<int:pk>', views.pay_page, name='pay_page'),
    path('complete/<int:pk>', views.pay_complete, name='pay_complete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)