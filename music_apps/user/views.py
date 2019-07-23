from django.shortcuts import render, redirect
from .form import *
from .models import *
from index.models import *
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


# Create your views here.

def loginView(request):
    user = MyUserCreationForm()
    if request.method == 'POST':
        # 登录
        if request.POST.get('loginUser', ''):
            loginUser = request.POST.get('loginUser', '')
            password = request.POST.get('password', '')
            user = MyUser.objects.filter(
                Q(mobile=loginUser) |
                Q(username=loginUser)
            )
            if user:
                user = user.first()
                if check_password(password, user.password):
                    login(request, user)
                    return redirect('/music/user/home')
                else:
                    tips = '密码错误'
            else:
                tips = '用户不存在'
        # 注册
        else:
            user = MyUserCreationForm(request.POST)
            print(user)
            if user.is_valid():
                user.save()
                tips = '注册成功'
            else:
                if user.errors.get('username', ''):
                    tips = user.errors.get('username', '注册失败')
                else:
                    tips = user.errors.get('mobile', '注册失败')
    return render(request, 'login.html', locals())


def logoutView(request):
    logout(request)
    return redirect('/music/user/login')


@login_required(login_url='/music/user/login')
def homeView(request, page):
    search_song = Dynamic.objects.select_related(
        'song').order_by('-dynamic_search').all()[:6]
    # 分页
    song_info = request.session.get('play_list',[])

    paginator = Paginator(song_info, 3)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger as e:
        contacts = paginator.page(1)
    except EmptyPage as e:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', locals())
