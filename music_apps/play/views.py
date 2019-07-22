import os
from django.utils.http import urlquote
from django.shortcuts import render
from django.http import StreamingHttpResponse
from index.models import *

# Create your views here.


def playView(request, song_id):

    # 热搜
    search_song = Dynamic.objects.select_related(
        'song').order_by('-dynamic_search').all()[:6]

    # 歌曲信息
    song_info = Song.objects.get(song_id=int(song_id))

    # 播放列表
    play_list = request.session.get('play_list', [])
    song_exist = False
    if play_list:
        for i in play_list:
            if int(song_id) == i['song_id']:
                song_exist = True
    if not song_exist:
        play_list.append(
            {
                'song_id': int(song_id),
                'song_name': song_info.song_name,
                'song_singer': song_info.song_singer,
                'song_time': song_info.song_time,
            }
        )
        request.session['play_list'] = play_list
    # 歌词部分
    if song_info.song_lyrics != '暂无歌词':
        with open('music_apps/static/songLyric/' + song_info.song_lyrics, 'r', encoding='utf-8') as f:
            song_lyrics = f.read()

    # 相关歌曲
    song_type = Song.objects.values('song_type').get(
        song_id=song_info.song_id)['song_type']
    song_relevant = Dynamic.objects.select_related('song').filter(
        song__song_type=song_type).order_by('-dynamic_plays').all()[:6]

    # 增加播放量
    song_exist = Song.objects.filter(song_id=song_info.song_id).first()
    if song_exist:
        dynamic_info = Dynamic.objects.filter(
            song_id=song_info.song_id).first()
        if dynamic_info:
            dynamic_info.dynamic_plays += 1

        else:
            dynamic_info = Dynamic(
                song_id=song_id,
                dynamic_plays=1,
                dynamic_search=0,
                dynamic_download=0,
            )
        dynamic_info.save()
    return render(request, 'play.html', context=locals())


def downloadView(request, song_id):
    """
    歌曲下载
    """
    song_info = Song.objects.filter(song_id=int(song_id)).first()
    if song_info:
        dynamic_info = Dynamic.objects.filter(song_id=int(song_id)).first()
        if dynamic_info:
            dynamic_info.dynamic_download += 1
        else:
            dynamic_info = Dynamic(
                song_id=song_id,
                dynamic_plays=0,
                dynamic_search=0,
                dynamic_download=1,
            )
        dynamic_info.save()

        # 下载
        file = 'music_apps/static/songFile/' + song_info.song_file

        def file_iterator(file, chunk_size=512):
            with open(file, 'rb') as f:
                while True:
                    file_content = f.read(chunk_size)
                    if file_content:
                        yield file_content
                    else:
                        break
        filename = song_info.song_name + '.mp3'
        response = StreamingHttpResponse(file_iterator(file))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(urlquote(filename))
        return response
