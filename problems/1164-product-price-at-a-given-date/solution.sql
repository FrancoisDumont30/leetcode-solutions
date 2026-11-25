# Filtre de date
WITH 
date_filter AS (
    SELECT product_id, change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    ORDER BY product_id ASC, change_date ASC),

# Distinct id
id_filter AS 
    (SELECT DISTINCT product_id FROM Products),

# JOIN id et change date
join1 AS (SELECT i.product_id, sub.change_date
    FROM id_filter i
    LEFT JOIN (
        SELECT product_id, 
        MAX(change_date) as change_date
        FROM date_filter
        GROUP BY product_id) AS sub
        ON i.product_id = sub.product_id)

SELECT j.product_id, COALESCE(p.new_price, 10) As price
FROM join1 j
LEFT JOIN Products p
ON p.product_id = j.product_id
AND p.change_date = j.change_date
