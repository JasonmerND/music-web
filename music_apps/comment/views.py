import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from index.models import *
from django.http import Http404
# Create your views here.


def commentView(request, song_id):

    # 热搜
    search_song = Dynamic.objects.select_related(
        'song').order_by('-dynamic_search').all()[:6]

    # 点评
    if request.method == "POST":
        comment_text = request.POST.get('comment', "")
        comment_user = request.user.username if request.user.username else '匿名用户'
        if comment_text:
            comment_obj = Comment(
                comment_text = comment_text,
                comment_user = comment_user,
                song_id = song_id,
                comment_date = time.strftime("%Y-%m-%d %H:%M:%S"),
            )
            comment_obj.save()
        return redirect('/music/comment/{}'.format(str(song_id)))

    else:
        # GET请求，判断是否有歌曲，没有即404
        song_info = Song.objects.filter(song_id=int(song_id)).first()
        if not song_info:
            raise Http404
        comment_all = Comment.objects.filter(song_id=int(song_id)).order_by('-comment_date')
        song_name = song_info.song_name
        page = int(request.GET.get('page', 1))
        paginator = Paginator(comment_all, 2)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger as e:
            contacts = paginator.page(1)
        except EmptyPage as e:
            contacts = paginator.page(paginator.num_pages)
        return render(request, 'comment.html', context=locals() )



