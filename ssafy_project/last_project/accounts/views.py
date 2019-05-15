from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from movies.models import Score
from .forms import UserCustomCreationForm

def signup(request):
    if request.method == 'POST':
        signup_form = UserCustomCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('movies:movie_list')
    else:
        signup_form = UserCustomCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form': signup_form})


def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'movies:movie_list')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})


def logout(request):
    auth_logout(request)
    return redirect('movies:movie_list')



#############################################################

def list(request, user_id):
    # 유저 모델, 정보 다 들고와
    users = get_user_model().objects.all()
    profile = get_object_or_404(get_user_model(), id=user_id)
    return render(request, 'accounts/list.html', {'users' : users, 'profile':profile})


def detail(request, user_id):
    profile = get_object_or_404(get_user_model(), id=user_id)

    if len(Score.objects.filter(user__in=request.user.followings.values('id'))) > 0:
        friendmovie = Score.objects.filter(user__in=request.user.followings.values('id')).order_by('-value')[0]
    else:
        friendmovie = []
    if len(Score.objects.all()) > 0:
        bestmovie = Score.objects.all().order_by('-value')[0]
    else:
        bestmovie = []
    return render(request, 'accounts/detail.html', {'profile': profile, 'friendmovie':friendmovie, 'bestmovie' : bestmovie})


# 팔로우
def follow(request, user_id):
    profile = get_object_or_404(get_user_model(), id=user_id)
    # 만약 내가(request.user)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
    else:
        profile.followers.add(request.user)
    return redirect('accounts:detail', user_id)


# 팔로우 사람 목록 출력
def followers(request, user_id):
    profile = get_object_or_404(get_user_model(), id=user_id)
    users = profile.followers.all()
    return render(request, 'accounts/list.html', {'users': users, 'profile':profile})


def followings(request, user_id):
    profile = get_object_or_404(get_user_model(), id=user_id)
    users = profile.followings.all()
    return render(request, 'accounts/list.html', {'users' : users, 'profile':profile})