from django.urls import path
from . import views

urlpatterns = [
    path('ranking', views.rankingView, name='ranking'),
]