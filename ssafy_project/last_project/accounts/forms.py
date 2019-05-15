from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # 3. 로그인 로그아웃
        fields = ('username',)