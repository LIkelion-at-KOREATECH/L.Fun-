from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import main1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 비회원일 경우
    path('nonmember/', main1.views.home1, name='home1'),
    path('nonmember/post/', main1.views.posting1, name='posting1'),
    # 회원일 경우
    path('member/', main1.views.home2, name='home2'),
    path('post/', main1.views.posting2, name='posting2'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
