from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.home, name="home"),
    path('enlarge/',myapp.views.enlarge, name="enlarge"),
    path('date/', myapp.views.date, name="date"),
]
