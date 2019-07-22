from django.shortcuts import render
from .models import *
# Create your views here.

def indexView(request):
    """
    音乐网站的首页
    """
    # 热搜排行
    hot_search_list = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:8]

    # 音乐分类
    label_list = Label.objects.all()
    # 热门歌曲
    hot_paly_list = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:10]
    # 新歌推荐
    new_song_list = Song.objects.order_by('-song_release').all()[:3]
    # 热门搜索、热门下载
    search_ranking = hot_search_list[:6]
    download_ranking = Dynamic.objects.select_related('song').order_by('-dynamic_download').all()[:6]
    all_ranking = [search_ranking, download_ranking]
    return render(request, 'index.html', context=locals())