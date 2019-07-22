from django.urls import path
from . import views

urlpatterns = [
    path('home/<int:id>', views.userView, name='home'),
]