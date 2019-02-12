## pyenv 설치
git clone https://github.com/pyenv/pyenv.git ~/.pyenv  
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc  
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc  
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc  
exec "$SHELL"  

git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv  
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc  
exec "$SHELL"  

pyenv install 3.6.7  
pyenv virtualenv 3.6.7 intro-venv  
pyenv activate intro-venv (pyenv deactivate)  

## 장고 설치
pip install --upgrade pip  
pip install django  

## 장고 프로젝트 생성
django-admin startproject intro .

## 장고 프로젝트 설정
settings.py에서 ALLOWED_HOSTS 수정  
https://first-django-hansung27.c9users.io  
LANGUAGE_CODE = 'en-us'  
TIME_ZONE = 'Asia/Seoul'  

## 장고 서버 실행
python manage.py runserver $IP:$PORT  

## 장고 앱 생성
python manage.py startapp pages  
settings.py에서 INSTALLED_APPS 수정  
'pages.apps.PagesConfig'  

## 장고 앱 코딩
views.py에서 render 설정
``` python
def index(request):
    return render(request, 'pages/index.html')
```
templates 폴더 만들어서 html 파일만들기  

urls.py 에서 urlpatterns에  
``` python
import pages import views
path('index/', views.index)
```
