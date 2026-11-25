# Write your MySQL query statement below
SELECT user_id, email
FROM Users
WHERE email RLIKE '^[0-9a-zA-Z]*@[a-zA-Z][a-zA-Z]*\\.com$'
ORDER BY user_id ;
