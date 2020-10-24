from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('place/', views.place, name="place"),
    path('place/fi/', views.placefi, name='placefi'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)