# Write your MySQL query statement below
With cte AS(SELECT requester_id as id
FROM RequestAccepted
UNION ALL
SELECT accepter_id as id
FROM RequestAccepted)
SELECT id, COUNT(*) AS num
FROM cte
GROUP BY id
ORDER BY num DESC
LIMIT 1;
