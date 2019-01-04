from flask import Flask, request
from bs4 import BeautifulSoup as bs
import requests
import json
import time
import os


app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL = 'https://api.hphk.io/telegram'

# 마스터키 전체
# 마스터키 ***점
CAFE_LIST = {
            '전체': -1,
            '부천점': 15,
            '안양점': 13,
            '대구동성로2호점': 14,
            '대구동성로점': 9,
            '궁동직영점': 1,
            '은행직영점': 2,
            '부산서면점': 19,
            '홍대상수점': 20,
            '강남점': 16,
            '건대점': 10,
            '홍대점': 11,
            '신촌점': 6,
            '잠실점': 21,
            '부평점': 17,
            '익산점': 12,
            '전주고사점': 8,
            '천안신부점': 18,
            '천안점': 3,
            '천안두정점': 7,
            '청주점': 4
        }


@app.route('/{}'.format(TELEGRAM_TOKEN), methods=['POST'])
def telegram():
    #텔레그램으로부터 요청이 들어올 경우, 해당 요청을 처리하는 코드
    
    #print(request.get_json())
    #print(json.loads(request))
    
    response = request.get_json()
    
    chat_id = response["message"]["from"]["id"]
    msg =response["message"]["text"]
    
    
    if (msg.startswith("마스터키")) :
        cafe_name = msg.split(' ')[1]
        
        if(cafe_name in CAFE_LIST.keys()):
            msg = []
            if(CAFE_LIST[cafe_name]==-1):
                for d in master_key_list():
                    msg.append('\n'.join(d.values()))
                #msg = ' '.join(CAFE_LIST.keys())
                
                # for d in master_key_list():
                #     cnt =0
                #     for z in d.values():
                #         if (cnt==3):
                #             msg.append('\n'.join(''))
                #         else:
                #             msg.append('\n'.join(z))
                #         cnt+=1
                
            else:
                for d in master_key_info(CAFE_LIST[cafe_name]):
                    msg.append('\n'.join(d.values()))
        
            msg = '\n'.join(msg)
        
        else:
            msg = '등록되지 않은 지점입니다.'
    
    elif(msg.startswith("서이룸")):
        if(len(msg.split(' '))>2):
            cafe_name = msg.split(' ')[1] +' '+ msg.split(' ')[2]
        else:
            cafe_name = msg.split(' ')[1]
            
        if (cafe_name == "전체"):
            msg = '\n'.join(seoul_escape_list())
        else:
            msg = '\n'.join(seoul_escape_info(cafe_name))
    
        
    elif(msg == "환율"):
        bab = []
        avg = []
        name = []
        buy = []
        sell = []
            
        url = "https://spib.wooribank.com/pib/jcc?withyou=CMCOM0184&__ID=c012238"
        
        response= requests.get(url).text
        
        soup = bs(response, 'html.parser')
        
        all_asas=soup.find_all('td')
        
        cnt =0
        for j in all_asas:
            if(cnt<len(all_asas)):
                bab.append(j.text)
            cnt+= 1
            
        cnt=1
        for z in range(45):
            name.append(bab[cnt])
            buy.append(bab[cnt+3])
            sell.append(bab[cnt+5])
            avg.append(bab[cnt+8])
            
            cnt+= 12
            
        # 배열을 스트링으로 출력
        for x in range(45):
            msg = msg +'\n' + name[x] +'  매매기준가: '+ avg[x] +'  살때: '+ buy[x] +'  팔때: '+ sell[x]
        
        # ['abc', 'black', 'power']
        # ''.join(list명)  => abcblackpower
        # '\n'.join(list명) => abc\black\power

        
    url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(TELEGRAM_TOKEN)
    requests.get(url, params = {"chat_id": chat_id, "text": msg})
        
    # 보낸 메세지내용 그대로 다시 리턴
    # chat_id = response["message"]["from"]["id"]
    # msg = response["message"]["text"]
    
    # url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(TELEGRAM_TOKEN)
    
    # requests.get(url, params = {"chat_id": chat_id, "text": msg})
    
    
    
    return '', 200


@app.route('/set_webhook')
def set_webhook():
    
    
    url = TELEGRAM_URL + '/bot' + TELEGRAM_TOKEN + '/setWebhook'
    params = {
        'url': 'https://ssafy-week2-hansung27.c9users.io/{}'.format(TELEGRAM_TOKEN)
    }
    
    response = requests.get(url, params = params).text
    
    return response







def master_key_list():
    url = "http://www.master-key.co.kr/home/office"
    
    response = requests.get(url).text
    
    document = bs(response, 'html.parser')
    
    # 별명의 종류가 class면 앞에 .   id인경우 앞에 #   나머지는 속성
    lis = document.select('.escape_list .escape_view')   
    
    cafe_list = []
    
    for li in lis:
        
        title = li.select_one('p').text
        address = li.select('dd')[0].text
        tel = li.select('dd')[1].text
        link = li.select_one('a').get('href')
        id = link.split("=")[1]
        #link = li.select_one('a')['href']
        
        # python how to eliminate string from string
        # String 끝부분 자르는 코드
        if title.endswith('NEW'):
            title = title[:-3]
            
        if address.endswith('마스터키 '):
            address = address[:-6]
        
        cafe = {
            'title': title,
            'info': address +'  '+ tel,
            'link': 'http://www.master-key.co.kr'+link,
            #'id': id
            'id': ' '
        }
        
        cafe_list.append(cafe)
    
    return cafe_list


def master_key_info(id):
    url = "http://www.master-key.co.kr/booking/booking_list_new"
    
    params = {
            "date": time.strftime("%Y-%m-%d"),
            "store": id,
            "room": ""
        }
    
    response = requests.post(url, params).text
    
    document = bs(response, 'html.parser')
    
    lis = document.select('.reserve .escape_view')
    
    theme_list = []
    
    for li in lis:
        title = li.select('p')[0].text
        info =''
        
        for col in li.select('.col'):
            info = info + '{} - {}\n'.format(col.select_one('.time').text, col.select_one('.state').text)
        
        theme = {
            'title': title,
            'info': info
        }
        
        theme_list.append(theme)
    
    return theme_list


def get_total_info():
    CAFE_CODE = {
        '강남1호점': 3,
        '홍대1호점': 1,
        '부산 서면점':5,
        '인천 부평점':4,
        '강남2호점': 11,
        '홍대2호점': 10
    }
    
    
    url = 'http://www.seoul-escape.com/reservation/change_date/'
    
    params = {
        'current_date': time.strftime("%Y/%m/%d")
    }
    
    
    response = requests.get(url, params = params).text
    
    document = json.loads(response)
    
    total = {}
    game_room_list = document["gameRoomList"]
    book_list = document["bookList"]
    
    # 기본 틀 잡기
    for cafe in CAFE_CODE:
        total[cafe] = []
        for room in game_room_list:
            if(CAFE_CODE[cafe] == room["branch_id"]):
                total[cafe].append({"title": room["room_name"],
                                    "info": []})
    
    # 앞에서 만들 틀에 데이터 집어넣기
    for cafe in total:
        for book in book_list:
            if(cafe == book["branch"]):
                for theme in total[cafe]:
                    if(theme["title"] == book["room"]):
                        if(book["booked"]):
                            booked = "예약완료"
                        else:
                            booked = "예약가능"
                        theme["info"].append("{} - {}".format(book["hour"], booked))
    
    
    return total



def seoul_escape_list():
    total = get_total_info()
    
    return total.keys()
    
    
def seoul_escape_info(id):
    total = get_total_info()
    cafe = total[id]
    
    theme_list = []
    
    for theme in cafe:
        theme_list.append("\n{}\n{}".format(theme["title"], '\n'.join(theme["info"])))
    
    
    return theme_list




