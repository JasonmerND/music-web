"""NaturalDeveloper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [

    # 音乐网站的路由
    path('music/admin/', admin.site.urls),
    path('music',include('index.urls')),
    path('music/ranking/',include('ranking.urls')),
    path('music/play/',include('play.urls')),
    path('music/search/',include('search.urls')),
    path('music/user/',include('user.urls')),
    path('music/comment/',include('comment.urls')),
    url(
        '^static/(?P<path>.*)$',
        static.serve,
        {
        'document_root':settings.STATIC_ROOT
        },
        name='static'),
]

from index import views

handler404 = views.page_not_found