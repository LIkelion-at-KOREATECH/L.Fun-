from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('enlarge/', views.enlarge, name='enlarge'),
    path('date/', views.date, name='date'),
    path('register/', views.register, name='register'),
    path('register/fi/', views.registerfi,name='registerfi')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)