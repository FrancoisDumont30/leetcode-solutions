# Write your MySQL query statement below
WITH top_order AS (SELECT customer_number, COUNT(order_number)
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC)
SELECT customer_number
FROM top_order
LIMIT 1
