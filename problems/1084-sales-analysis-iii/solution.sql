# Write your MySQL query statement below
SELECT DISTINCT s.product_id, p.product_name
FROM sales s 
JOIN product p
ON p.product_id = s.product_id
WHERE s.product_id NOT IN (SELECT product_id
    FROM sales
    WHERE sale_date < '2019-01-01'
    OR sale_date > '2019-03-31')
