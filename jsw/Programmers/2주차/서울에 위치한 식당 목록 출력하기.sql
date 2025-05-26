-- 옛날에 푼 코드드
SELECT A.REST_ID , A.REST_NAME , A.FOOD_TYPE , A.FAVORITES , A.ADDRESS , 
ROUND(AVG(B.REVIEW_SCORE) , 2)
FROM REST_INFO AS A
JOIN REST_REVIEW AS B
ON A.REST_ID = B.REST_ID
WHERE A.ADDRESS LIKE '서울%'
GROUP BY A.REST_ID
ORDER BY AVG(B.REVIEW_SCORE) DESC , A.FAVORITES DESC

--이번에 새로 푼 코드
select i.rest_id, REST_NAME, FOOD_TYPE, FAVORITES, 
ADDRESS, round(avg(r.review_score),2) score
from REST_INFO  i
left join REST_REVIEW r
on i.rest_id = r.rest_id
where address like '서울%' and review_score is not null
group by i.rest_id
order by avg(review_score) desc, favorites desc

-- 회고록
-- 흠...
-- left join과 그냥 join의 차이점을 찾아봤는데 
-- join은 교집합 left join은 합집합이라고 하는데 
-- 그건 join하는 키에 대해서만 그런걸로 알고있는데
-- 제가 잘못알고있는걸까요..? 아시는분은 좀 가르쳐 주시면 감사하겠습니다ㅎㅎ...
