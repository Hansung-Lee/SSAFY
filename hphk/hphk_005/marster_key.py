from bs4 import BeautifulSoup as bs
import requests

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
            'link': link,
            'id': id
        }
        
        cafe_list.append(cafe)
    
    return cafe_list


def master_key_info(id):
    url = "http://www.master-key.co.kr/booking/booking_list_new"
    
    params = {
            "date": "2018-12-22",
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


# 사용자로부터 '마스터키 ***점'이라는 메시지를 받으면,
# 해당 지점에 대한 정보를 요청하고(크롤링) 메시지(예약정보)를 보내준다.



# Main Method
# for li in master_key_list():
#     print('{}: {}'.format(li['title'],li['id']))


#print(master_key_info(21))






