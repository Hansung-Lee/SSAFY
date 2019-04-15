from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    if request.method == "POST":
        # 회원가입 시키기(DB에 사용자 정보를 저장)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index.html')
    else:
        # 회원정보를 받는 form 보여주기
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
