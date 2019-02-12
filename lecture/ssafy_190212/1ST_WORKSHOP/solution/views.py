from django.shortcuts import render
import random
import datetime
import requests
import os

naver_id = os.getenv("naver_id")
naver_secret = os.getenv("naver_secret")

# Create your views here.
def info(request):
    return render(request, 'info.html')
    
def student(request, name):
    age=random.randint(20,30)
    return render(request, 'student.html', {'name': name, 'age': age})
    
def valentines(request):
    result = '아니오'
    utc_ko = datetime.timedelta(seconds=32400)
    dt = datetime.datetime.now()+utc_ko
    nowtime = dt.strftime("%m/%d")
    if nowtime=="02/14":
        result = '네'
    return render(request, 'valentines.html', {'result': result})
    
def graduate(request):
    utc_ko = datetime.timedelta(seconds=32400)
    now = datetime.datetime.now()+utc_ko
    end = datetime.datetime(2019, 5, 19)
    days = end - now
    print(days.days)
    return render(request, 'graduate.html', {'days': days.days})
    
def image(request):
    return render(request, 'image.html')
    
def index(request):
    return render(request, 'index.html')
    
def catch(request):
    msg = request.GET.get('message')
    styles = ['rounded', 'cosmic', 'gothic', 'alligator', 'avatar']
    style = random.choice(styles)
    # artii
    url = f"http://artii.herokuapp.com/make?text={msg}&font={style}"
    result = requests.get(url).text
    return render(request, 'catch.html', {'message': result})
    
def translate(request):
    return render(request, 'translate.html')
    
def result(request):
    word = request.GET.get('word')
    sel = request.GET.get('sel')
    
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    headers = {
        'X-Naver-Client-Id': naver_id,
        'X-Naver-Client-Secret': naver_secret
    }
        
    if (sel=='1'):
        data = {
            'source': 'ko',
            'target': 'en',
            'text': word
        }
    elif (sel=='2'):
        data = {
            'source': 'en',
            'target': 'ko',
            'text': word
        }
    
    res = requests.post(url, headers=headers, data=data)
    trans_word = res.json().get('message').get('result').get('translatedText')
    
    return render(request, 'result.html', {'word': word, 'trans_word': trans_word})