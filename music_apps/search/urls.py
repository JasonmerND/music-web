from django.urls import path
from . import views

urlpatterns = [
    path('search/<int:id>', views.searchView, name='search'),
]