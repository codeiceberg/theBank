from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LoginOutterfaceView.as_view(), name='logout'),
]
