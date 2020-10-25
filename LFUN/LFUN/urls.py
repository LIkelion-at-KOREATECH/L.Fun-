from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main1 import views
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/', include('place.urls')), # 펀딩/장소 신청
    path('main/', include('main1.urls')),
    path('search/', include('search.urls')),
    path('pub/', include('pub_result.urls')),

    # 미림
    path('',myapp.views.home, name="home"),
    path('enlarge/',myapp.views.enlarge, name="enlarge"),
    path('date/', myapp.views.date, name="date"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)