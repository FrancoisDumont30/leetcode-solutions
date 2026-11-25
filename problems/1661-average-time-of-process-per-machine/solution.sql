
WITH Activity2 AS
    (SELECT A1.*, A2.timestamp AS end
    FROM Activity A1
    JOIN Activity A2
    ON A1.machine_id = A2.machine_id AND A1.process_id = A2.process_id 
    AND A1.activity_type != A2.activity_type
    HAVING A1.activity_type = 'start') 

SELECT machine_id, ROUND(AVG(end-timestamp),3) AS processing_time
FROM Activity2
GROUP BY machine_id
;
