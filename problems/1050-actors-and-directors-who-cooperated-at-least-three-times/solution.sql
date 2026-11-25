# Write your MySQL query statement below
WITH selection AS (SELECT actor_id, director_id, COUNT(timestamp) AS num
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING num >= 3)
SELECT actor_id, director_id
FROM selection;
