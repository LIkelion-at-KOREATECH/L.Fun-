from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from main1 import views
from . import views

app_name = 'search'

urlpatterns = [
    path('nonmember/', views.searchResult1, name='searchResult1'),
    path('', views.searchResult2, name='searchResult2')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)