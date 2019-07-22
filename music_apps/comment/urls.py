from django.urls import path
from . import views

urlpatterns = [
    path('<int:song_id>', views.commentView, name='comment'),
]
