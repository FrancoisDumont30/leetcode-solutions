WITH cte AS (
    SELECT user_id, ROUND(AVG(activity_duration), 2) AS paid_avg_duration
        FROM UserActivity
        WHERE activity_type = 'paid'
        GROUP BY user_id)

SELECT c.user_id, sub.trial_avg_duration, c.paid_avg_duration
FROM cte c

JOIN (SELECT user_id, ROUND(AVG(activity_duration), 2) AS trial_avg_duration
        FROM UserActivity
        WHERE activity_type = 'free_trial'
        GROUP BY user_id) sub

ON sub.user_id =c.user_id
