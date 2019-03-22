from django.shortcuts import render, redirect
from .models import Shout
from .forms import ShoutModelForm


# Create your views here.


def home(request):
    # form을 보여주기 & 문의사항 전부 보여주기
    shouts = Shout.objects.all()
    context = {
        'shouts': shouts,
    }
    return render(request, 'shout/home.html', context)


def create(request):
    if request.method == "POST":
        # 고객센터 문의 작성하기
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('shout:home')
    else:
        form = ShoutModelForm()
        context = {
            'form': form,
        }
        return render(request, 'shout/form.html', context)


def update(request, shout_id):
    if request.method == "POST":
        # 수정하기(update)
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('shout:home')
    else:
        # 편집하기(edit)
        shout = Shout.objects.get(id=shout_id)
        form = ShoutModelForm(instance=shout)
        context = {
            'form': form,
        }
        return render(request, 'shout/form.html', context)
