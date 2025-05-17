-- 코드를 입력하세요
with info as (
    SELECT *
    FROM REST_INFO
    WHERE ADDRESS LIKE "서울%"
),
result as (
    SELECT info.REST_ID,
           FAVORITES,
           ADDRESS, 
           REVIEW_SCORE as SCORE,
           REST_NAME,
           FOOD_TYPE
    FROM info
    JOIN REST_REVIEW review
    ON info.REST_ID = review.REST_ID
),
answer as (
SELECT REST_ID, 
       REST_NAME,
       FOOD_TYPE,  
       FAVORITES,
       ADDRESS,
       ROUND(AVG(SCORE),2) AS SCORE
FROM RESULT
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC)

SELECT * FROM answer;





