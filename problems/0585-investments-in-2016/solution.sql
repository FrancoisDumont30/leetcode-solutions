WITH tiv_cte AS (
    SELECT pid, tiv_2015, count(*) AS num
    FROM Insurance
    GROUP BY tiv_2015
    Having num > 1),
    loc_cte AS (
        SELECT pid, count(*) AS num
        FROM Insurance
        GROUP BY lat, lon
        Having num = 1
    )

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (SELECT tiv_2015 FROM tiv_cte)
AND pid in (SELECT pid FROM loc_cte)
