import sqlite3

# <파이썬 콘솔에서 sqlite 작업시 과정>
# 1. > sqlite3 [데이터베이스 파일명]
#   => 데이터베이스에 접속
# 2. SQL 쿼리 사용
#   => SELECT * FROM users;
#   => 결과를 가져다 줌
# 3. > .exit
#   => 작업이 끝나면 콘솔 종료
# sqlite3.connect('데이터베이스 파일명')
db = sqlite3.connect('test.sqlite3')

def search():
    """
    DB에서 검색어를 받아 검색해 주는 함수
    """
    
    word = input("검색할 성(씨)을 입력하세요: ")
    
    cur = db.cursor() # DB 조작을 할 수 있는 커서를 만든다.
    
    cur.execute("SELECT COUNT(*) FROM users WHERE last_name == '{}'".format(word))
    total = cur.fetchone() # cur.fetchall() cur.fetchone()
    cur.execute("SELECT * FROM users WHERE last_name == '{}'".format(word))
    data = cur.fetchall()
    
    
    # 1. 해당 검색 결과의 수를 출력하고,
    # 2. 데이터들을 출력한다.
    # => '박'씨 성을 가진 사람은 XX명 입니다. 명단은 다음과 같습니다.
    print("'{}'씨 성을 가진 사람은 {}명 입니다. 명단은 다음과 같습니다.".format(word, total[0]))
    for row in data:
        print(row)
    
search()