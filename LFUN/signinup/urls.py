from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.first, name="first"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('signin/fi/', views.fi, name='fi'),
]
