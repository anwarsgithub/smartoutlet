from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('signup/', views.signup, name='main-signup'),
    path('about/', views.about, name='main-about'),
    path('accounts/', include('django.contrib.auth.urls'), name='main-login'),
]