from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import main1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main1.views.home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
