from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/', include('place.urls')), # 펀딩/장소 신청
    path('main/', include('main1.urls')),
]
