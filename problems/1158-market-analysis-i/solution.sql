# Write your MySQL query statement below
WITH cte AS (
    SELECT  buyer_id, 
            count(*) AS tot
    FROM Orders
    WHERE YEAR(order_date)=2019
    GROUP BY buyer_id)
SELECT u.user_id AS buyer_id, u.join_date, COALESCE(c.tot, 0) AS orders_in_2019
FROM Users u
LEFT JOIN cte c
ON u.user_id = c.buyer_id
