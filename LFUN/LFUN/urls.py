from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from .main1 import views
# from mirim import views
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 마이페이지, 기타
    path('pub/', include('pub_result.urls')),
    
    # 메인
    path('main/', include('main1.urls')),
    path('search/', include('search.urls')),

    # 신청 - 장소
    path('apply/', include('place.urls')),

    # 신청 - 펀딩
    path('apply_f/', include('mirim.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)