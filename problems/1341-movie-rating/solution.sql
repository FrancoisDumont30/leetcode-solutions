WITH cte AS (
    SELECT mr.user_id, u.name, COUNT(*) AS num
    FROM MovieRating mr
    JOIN Users u
    ON mr.user_id = u.user_id
    GROUP by user_id
    ORDER by num DESC, name ASC
    LIMIT 1),

movie_cte AS (
    SELECT m.title, AVG(mr.rating) AS mean
    FROM Movies m
    JOIN MovieRating mr
    ON mr.movie_id = m.movie_id
    WHERE mr.created_at >= '2020-02-01' 
    AND mr.created_at <= '2020-02-29'
    GROUP BY m.title
    ORDER BY mean DESC, m.title ASC
    LIMIT 1)

SELECT name AS results
FROM cte
UNION ALL
SELECT title
FROM movie_cte AS results
