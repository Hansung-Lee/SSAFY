-- Problem 1
-- 아래 표와 같은 스키마를 가진 DB 테이블을 생성하고, 아래와 같이 Data 를 입력해 봅시다.

CREATE TABLE bands(
id INTEGER,
name TEXT,
debut INTEGER
);

INSERT INTO bands VALUES (1, 'Queen', 1973);
INSERT INTO bands VALUES (2, 'Coldplay', 1998);
INSERT INTO bands VALUES (3, 'MCR', 2001);


-- Problem 2
-- bands 테이블에서 모든 데이터 레코드의 id 와 name 만 조회하는 Query 를 작성하라.

SELECT id, name FROM bands;


-- Problem 3
-- bands 테이블에서 debut 가 2000 보다 작은 밴드들의 이름만을 조회하는 Query 를 작성하라.

SELECT name FROM bands WHERE debut<2000;