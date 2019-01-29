# Homework_16

1. 다음과 같은 스키마를 가지는 DB 테이블 friends 를 생성한다.

``` sql
CREATE TABLE friends(
id INTEGER,
name TEXT,
location TEXT
);
```

2. 해당 테이블에 다음과 같이 데이터를 입력한다.

``` sql
INSERT INTO friends VALUES (1, 'Justin', 'Seoul');
INSERT INTO friends VALUES (2, 'Simon', 'New York');
INSERT INTO friends VALUES (3, 'Chang', 'Las Vegas');
INSERT INTO friends VALUES (4, 'John', 'Sydney');
```

3. 스키마를 다음과 같이 변경한다.

``` sql
ALTER TABLE friends ADD married INTEGER;
```

4. 데이터를 다음과 같이 추가한다.

``` sql
UPDATE friends SET married = 1 WHERE id == 1;
UPDATE friends SET married = 0 WHERE id == 2;
UPDATE friends SET married = 0 WHERE id == 3;
UPDATE friends SET married = 1 WHERE id == 4;
```

5. married 가 0 인 데이터를 모두 삭제한다.

``` sql
DELETE FROM friends WHERE married == 0;
```

6. 테이블을 삭제한다.

``` sql
DROP TABLE friends;
```