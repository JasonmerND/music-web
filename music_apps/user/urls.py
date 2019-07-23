from django.urls import path
from . import views

urlpatterns = [
    path('home/<int:page>', views.homeView, name='home'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
]