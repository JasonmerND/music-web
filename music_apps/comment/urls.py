from django.urls import path
from . import views

urlpatterns = [
    path('comment', views.commentView, name='comment'),
]