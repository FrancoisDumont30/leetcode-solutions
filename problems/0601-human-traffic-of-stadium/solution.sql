# Write your MySQL query statement below
WITH cte AS (
    SELECT 
    LAG(id) OVER() AS a,
    id,
    LEAD(id) OVER() AS c,
    visit_date,
    people
    FROM Stadium
    WHERE people >= 100
),
    filter AS (
    SELECT 
    *
    FROM cte
    WHERE a = id-1 AND c = id+1)
, aggreg AS (
    SELECT a AS res FROM filter
    UNION ALL
    SELECT id AS res FROM filter
    UNION ALL
    SELECT c AS res FROM filter
)

SELECT * FROM Stadium WHERE id IN (SELECT DISTINCT res FROM aggreg)
