# Homework_15

1. 우리가 사용하는 SQLite는 RDBMS에 속한다. RDBMS의 특징을 2가지만 작성하세요.   

```
1. 데이터를 컬럼(column)과 로우(row)를 이루는 하나 이상의 테이블(또는 관계)로 정리한다.
2. 고유 키(Primary key)가 각 로우를 식별한다.
```



2. True False
   2.1. RDBMS를 조작하기 위해서는 SQL문을 사용한다. [ T ]
   2.2. SQL에서 명령어는 대문자로 써야만 동작한다. [ F ]
   2.3. 일반적인 SQL문에서 명령어는 세미콜론(;) 으로 끝난다. [ T ]
   2.4. SQLite에서 dot(.) 으로 시작하는 명령어는 SQL이 아니다. [ T ]
   2.5. 한 개의 DB에는 한 개의 테이블만 존재한다.  [ F ] 




3. 다음 코드의 실행결과로 나타나는 값을 작성하세요.    

```
sqlite> .nullvalue “NULL”
sqlite> CREATE TABLE ssafy(
…> id INTEGER,
…> location TEXT,
…> class INTEGER
…> );
sqlite> INSERT INTO ssafy(id, location)
…> VALUES (1, ‘JEJU’);
sqlite> SELECT class FROM ssafyWHERE id=1;
```
```
정답: NULL
```
