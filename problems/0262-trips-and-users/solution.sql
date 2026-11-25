# Write your MySQL query statement below
WITH cte AS (
    SELECT *, 
    CASE
        WHEN status = 'completed' THEN 0
        ELSE 1
        END AS Cancellation
    FROM Trips
    WHERE client_id IN (SELECT users_id FROM Users WHERE banned='No')
    AND driver_id IN (SELECT users_id FROM Users WHERE banned='No')
    AND request_at > '2013-09-30' AND request_at < '2013-10-04')
SELECT request_at AS Day, ROUND(AVG(Cancellation), 2) AS `Cancellation Rate`
FROM cte
GROUP BY Day
