# Write your MySQL query statement below
WITH cte AS (SELECT 
    score,
    ROW_NUMBER() OVER (ORDER BY score DESC) AS `ranking`
FROM Scores
GROUP BY score)
SELECT s.score, c.ranking as `rank`
FROM Scores s
JOIN cte c
ON s.score = c.score
ORDER BY score DESC
