from flask import Flask, render_template, send_file, request
from datetime import datetime as dt
import random


app = Flask(__name__)


hogu = []



@app.route('/')  # 주문 받는 방법(응답을 받는 방법)
def index():
    
    
    lotto = random.sample(range(1,46), 6)
    
    # return "Hello World!"  # 서비스 주는 방법(응답을 보내는 방법)
    
    # return str(random.sample(range(1,46), 6))
    # return render_template('index.html') # 동적, 파이썬코드를 html에 심을수 있음
    # return send_file('home.html') # 정적, 파이썬코드를 html에 심기 불가능
    
    return render_template('index.html', lotto=lotto)



@app.route('/hello/<name>')
def hello(name):
    return "hello, {}".format(name)
   

@app.route('/cube/<num>')
def cube(num):
    return "{}의 제곱은 {}입니다.".format(num, int(num)**3)


@app.route('/reverse/<text>')
def reverse(text):
    
    result = ''
    
    for x in text:
        result = x+result
        
    # text.reversed()
    # text[::-1]
    
    return result

    
    
# 앞으로 해도 이효리 거꾸로 해도 이효리
# /ispal/racecar => true
# /ispal/john => false
    
@app.route('/ispal/<text>')
def ispal(text):
    
    result = ''
    
    for x in text:
        result = x+result
    
    tf = False
    msg = '입력하신 단어는 뒤집어서 읽으면 원래와 다릅니다.'
    
    if (text==result):
        tf= True
        msg = '입력하신 단어는 앞으로 읽어도 뒤로읽어도 같습니다.'
    
    return msg
    
    # if text==text[::-1]:
    #     return str(True)
    # else:
    #     return str(False)
    
    # 삼항연산자
    # 참거짓 ? 참일때 : 거짓일때
    # return str(True) if text==text[::-1] else str(False)
    
    

# /isitnewyear => 1월1일이면 "예" 아니면 "아니오"

@app.route('/isitnewyear')
def isitnewyear():
    if dt.now().month == 1 and dt.now().day == 1:
        return "예"
    else:
        return "아니오"
    


# /goonghap => 나와 상대방의 이름 + 페이크 궁합 값(60~90)을 알려준다.

@app.route('/goonghap')
def goonghap():
    
    me = request.args.get('me')
    you = request.args.get('you')
    score = random.randrange(60,100)
    
    # 입력 받은 이름들을 리스트에 저장해두어 /god 페이지에서 볼수있게 만듬
    hogu.append([me,you])
    
    # request: 사용자의 요청정보
    # return "{}님과 {}님의 궁합 점수는 {}점 입니다.".format(request.args.get('me'), request.args.get('you'), score)
    return render_template('goonghap.html', me=me, you=you, score=score)


@app.route('/god')
def god():
    return str(hogu)


