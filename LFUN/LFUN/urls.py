from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main1 import views
from pay import views
import mirim.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/', include('place.urls')), # 펀딩/장소 신청
    path('main/', include('main1.urls')),
    path('search/', include('search.urls')),
    path('pub/', include('pub_result.urls')),
    path('pay/', include('pay.urls')),

    # 미림
    path('',mirim.views.home, name="home"),
    path('enlarge/',mirim.views.enlarge, name="enlarge"),
    path('date/', mirim.views.date, name="date"),
    path('register/', mirim.views.register, name='register'),
    path('register/fi/', mirim.views.registerfi,name='registerfi')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)