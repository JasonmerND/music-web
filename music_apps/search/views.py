from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.db.models import Q
from index.models import *

# Create your views here.


def searchView(request, page):

    if request.method == 'POST':
        # POST请求
        request.session['kword'] = request.POST.get('kword', '')
        return redirect('/music/search/1')
    else:
        # GET请求
        # 热搜
        search_song = Dynamic.objects.select_related(
            'song').order_by('-dynamic_search').all()[:6]
        
        kword = request.session.get('kword', '')
        if kword:
            song_info = Song.objects.values(
                'song_id',
                'song_name',
                'song_singer',
                'song_time',
            ).filter(
                Q(song_name__icontains=kword) | 
                Q(song_singer=kword)
            ).order_by('-song_release').all()
        else:
            song_info = Song.objects.values(
                'song_id',
                'song_name',
                'song_singer',
                'song_time',
            ).order_by('-song_release').all()[:50]

        # 分页
        paginator = Paginator(song_info, 5)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger as e:
            contacts = paginator.page(1)
        except EmptyPage as e:
            contacts = paginator.page(paginator.num_pages)

        # 添加搜索次数
        song_exist = Song.objects.filter(song_name=kword)
        if song_exist:
            song_id = song_exist[0].song_id
            dynamic_info = Dynamic.objects.filter(song_id=int(song_id))
            if dynamic_info:
                dynamic_info.dynamic_search += 1
            else:
                dynamic_info = Dynamic(
                    dynamic_plays=0,
                    dynamic_search=1,
                    dynamic_download=0,
                    song_id=int(song_id),
                )
            dynamic_info.save()
        return render(request, 'search.html', locals())
