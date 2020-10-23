from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # 비회원일 경우
    path('nonmember/', views.home1, name='home1'),
    path('nonmember/post/', views.posting1, name='posting1'),
    # 회원일 경우
    path('member/', views.home2, name='home2'),
    path('post/', views.posting2, name='posting2'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)