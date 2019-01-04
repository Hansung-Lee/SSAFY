from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
import requests
import time
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/lotto')
def lotto():
    return render_template('lotto.html')


@app.route('/toon')
def toon():
    
    cat = request.args.get('type')
    if(cat == 'naver'):
        
        today = time.strftime("%a").lower()
        print(today)
        
        #1. 네이버 웹툰을 가져올 수 있는 주소(url)를 파악하고 url 변수에 저장
        url = "https://comic.naver.com/webtoon/weekdayList.nhn?week=" + today
        
        #2. 해당 주소로 요청을 보내 정보를 가져온다.
        response = requests.get(url).text
        
        
        #3. 받은 정보를 bs를 이용해 검색하기 좋게 만든다.
        soup = bs(response, 'html.parser')
        
        #4. 네이버 웹툰 페이지로 가서, 내가 원하는 정보가 어디에 있는지 파악한다.
        toons = []
        
        li= soup.select('.img_list li')
        
        for item in li:
            toon = {
                "title": item.select('dt a')[0].text,
                "url": "https://comic.naver.com/" + item.select('dt a')[0]["href"],
                "img_url": item.select('img')[0]["src"]
            }
            toons.append(toon)
    
    
    elif(cat == 'daum'):
        
        today = time.strftime("%a").lower()
        
        #1. 내가 원하는 정보를 얻을 수 있는 주소를 url이라고 하는 변수에 담는다.
        url ="http://webtoon.daum.net/data/pc/webtoon/list_serialized/" + today
        
        #2. 해당 url에 요청을 보내 응답을 받아 저장한다.
        response= requests.get(url).text
        
        #3. 구글신에게 python으로 어떻게 json을 파싱(딕셔너리형으로 변환)하는 지 물어본다.
        #4. 파싱한다.(변환한다.)
        document =json.loads(response)
        
        #5. 내가 원하는 데이터를 꺼내서 조합한다.
        data = document["data"]
        
        toons = []
        
        for toon in data:
            
            toons.append({
                "title": toon["title"],
                "url": "http://webtoon.daum.net/webtoon/view/{}".format(toon["nickname"]),
                "img_url": toon["pcThumbnailImage"]["url"]
            })
            
    
    return render_template('toon.html', cat = cat, t = toons)
    
    

@app.route('/apart')
def apart():
    
    #1. 내가 원하는 정보를 얻을 수 있는 url을 url 변수에 저장한다.
    url = 'http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do?menuGubun=A&p_apt_code=50805&p_house_cd=1&p_acc_year=2018&areaCode=&priceCode='
    
    #1-1. request header에 추가할 정보를 dictionary 형태로 저장한다.
    headers = {
        "Host": "rt.molit.go.kr",
        "Referer": "http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND"
    }
    
    #2. requests의 get 기능을 이용하여 해당 url에 header와 함께 요청을 보낸다.
    response= requests.get(url, headers = headers).text
    
    #3. 응답으로 온 코드의 형태를 살펴본다. (json/xml/html)
    document = json.loads(response)
    
    print(document["result"])
    
    for d in document["result"]:
        print(d["BLDG_NM"])
    
    
    return render_template('/apart.html')



@app.route('/exchange')
def exchange():
    
    # url = "https://spib.wooribank.com/pib/Dream?withyou=CMCOM0184"
     
    # response= requests.get(url).text
    
    # soup = bs(response, 'html.parser')
    
    # pyosi = []
    # name = []
    # send = []
    # receive = []
        
    # #li= soup.select('.img_list li')
    # all_fieldsets = soup.find(id="id01")
    # vvv = all_fieldsets.select("option")

    # cnt =0
    # for i in vvv:
    #     if(cnt >0):
    #         str1 = i.text.split("(")[0]
    #         pyosi.append(str1)
            
    #     cnt+=1
        
    bab = []
    pyosi= []
    avg = []
    name = []
    buy = []
    sell = []
    exchanges = []
        
    url = "https://spib.wooribank.com/pib/jcc?withyou=CMCOM0184&__ID=c012238"
        
    response= requests.get(url).text
        
    soup = bs(response, 'html.parser')
        
    all_asas=soup.find_all('td')
        
    cnt =0
    for j in all_asas:
        if(cnt<len(all_asas)):
            bab.append(j.text)
        cnt+= 1
            
    cnt=0
    for z in range(45):
        exchange = {
            'pyosi':bab[cnt],
            'name':bab[cnt+1],
            'avg':bab[cnt+8] ,
            'buy':bab[cnt+4],
            'sell':bab[cnt+6]
            
        }
            
        cnt+= 12
        exchanges.append(exchange)
    
    
    
        
        
    # for i in li:
    #     item = {
    #         "pyosi": i.select('dt a')[0].text,
    #         "name": "https://comic.naver.com/" + i.select('dt a')[0]["href"],
    #         "send": i.select('img')[0]["src"]
    #         "receive": i.select('img')[0]["src"]
    #     }
    #     exchanges.append(item)
    
    
    
    return render_template('exchange.html', ex = exchanges)



