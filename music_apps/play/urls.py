from django.urls import path
from . import views

urlpatterns = [
    path('paly/<int:id>', views.palyView, name='play'),
]