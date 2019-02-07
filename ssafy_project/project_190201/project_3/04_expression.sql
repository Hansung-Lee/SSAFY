-- 1. 모든 영화의 총 누적관객수를 출력하세요.
SELECT SUM(누적관객수) FROM movies;


-- 2. 가장 많은 누적관객수인 영화이름과 누적관객수를 출력하세요.
SELECT 영화이름, 누적관객수 FROM movies ORDER BY 누적관객수 DESC LIMIT 1;


-- 3. 가장 상영시간이 짧은 영화의 장르와 상영시간을 출력하세요.
SELECT 장르, 상영시간 FROM movies ORDER BY 상영시간 LIMIT 1;


-- 4. 제작국가가 한국인 영화의 평균 누적관객수를 출력하세요.
SELECT AVG(누적관객수) FROM movies WHERE 제작국가 = "한국";


-- 5. 관람등급이 청소년관람불가인 영화의 개수를 출력하세요.
SELECT COUNT(*) FROM movies WHERE 관람등급 = "청소년관람불가";


-- 6. 상영시간이 100분 이상이고 장르가 애니메이션인 영화의 개수를 출력하세요.
SELECT COUNT(*) FROM movies WHERE 상영시간 >= 100 AND 장르 = "애니메이션";