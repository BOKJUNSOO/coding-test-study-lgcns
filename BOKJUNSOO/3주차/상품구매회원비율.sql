-- 다시 커밋
WITH user AS (
    SELECT *
    FROM USER_INFO
    WHERE JOINED LIKE '2021%'
),
joint AS (
    SELECT
        user.user_id,
        sale.product_id,
        sale.sales_amount,
        sale.sales_date
    FROM user
    JOIN online_sale sale
    ON user.user_id = sale.user_id
),
split AS (
    SELECT
        YEAR(sales_date) AS YEAR,
        MONTH(sales_date) AS MONTH,
        user_id,
        sales_amount
    FROM joint
),
grouped AS (
    SELECT
        YEAR,
        MONTH,
        COUNT (DISTINCT user_id) AS PURCHASED_USERS
    FROM split
    GROUP BY YEAR ,MONTH
),
finally as (
    SELECT 
        YEAR,
        MONTH,
        PURCHASED_USERS,
        round((PURCHASED_USERS / (SELECT COUNT(*) FROM user)),1) AS PUCHASED_RATIO
    FROM grouped
),
ordering as (
    SELECT *
    FROM finally
    ORDER BY YEAR, MONTH
)
SELECT * FROM ordering;