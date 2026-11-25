# Write your MySQL query statement below
WITH tempo AS (SELECT P.*, U.purchase_date, U.units, (U.units*P.price) AS total_price
FROM Prices P
LEFT JOIN UnitsSold U
ON U.product_id = P.product_id AND U.purchase_date BETWEEN P.start_date AND P.end_date) 

SELECT product_id, IFNULL(ROUND((SUM(total_price)/(SUM(units))),2),0) AS average_price
FROM tempo
GROUP BY product_id

;
