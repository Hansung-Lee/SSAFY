-- Problem 1
-- 저번 워크샵에서 아래 표와 같은 DB를 제작한 상태다.
CREATE TABLE bands(
id INTEGER,
name TEXT,
debut INTEGER
);

INSERT INTO bands VALUES (1, 'Queen', 1973);
INSERT INTO bands VALUES (2, 'Coldplay', 1998);
INSERT INTO bands VALUES (3, 'MCR', 2001);

-- 해당 테이블을 수정하여, 다음과 같이 컬럼을 추가하고, 데이터를 삽입하라.
ALTER TABLE bands ADD members INTEGER;

UPDATE bands SET members = 4 WHERE id == 1;
UPDATE bands SET members = 5 WHERE id == 2;
UPDATE bands SET members = 9 WHERE id == 3;


-- Problem 2
-- Id 가 3인 레코드의 members 를 5로 수정하라.
UPDATE bands SET members = 5 WHERE id == 3;


-- Problem 3
-- Id 가 2인 레코드를 삭제하라.
DELETE FROM bands WHERE id == 2;