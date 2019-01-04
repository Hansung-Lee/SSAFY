import requests
import json

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
        'current_date': '2018/12/21'
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
        theme_list.append("{}\n{}".format(theme["title"], '\n'.join(theme["info"])))
    
    
    return theme_list





print('\n'.join(seoul_escape_info('강남1호점')))



