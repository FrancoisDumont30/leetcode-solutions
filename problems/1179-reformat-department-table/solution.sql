# Write your MySQL query statement below
WITH new_table AS (SELECT id, month,
CASE 
    WHEN month = 'Jan' THEN revenue
END as 'Jan_Revenue',
CASE 
    WHEN month = 'Feb' THEN revenue
END as 'Feb_Revenue',
CASE 
    WHEN month = 'Mar' THEN revenue
END as 'Mar_Revenue',
CASE 
    WHEN month = 'Apr' THEN revenue
END as 'Apr_Revenue',
CASE 
    WHEN month = 'May' THEN revenue
END as 'May_Revenue',
CASE 
    WHEN month = 'Jun' THEN revenue
END as 'Jun_Revenue',
CASE 
    WHEN month = 'Jul' THEN revenue
END as 'Jul_Revenue',
CASE 
    WHEN month = 'Aug' THEN revenue
END as 'Aug_Revenue',
CASE 
    WHEN month = 'Sep' THEN revenue
END as 'Sep_Revenue',
CASE 
    WHEN month = 'Oct' THEN revenue
END as 'Oct_Revenue',
CASE 
    WHEN month = 'Nov' THEN revenue
END as 'Nov_Revenue',
CASE 
    WHEN month = 'Dec' THEN revenue
END as 'Dec_Revenue'
FROM Department)
SELECT id, 
SUM(Jan_Revenue) AS Jan_Revenue, 
SUM(Feb_Revenue) AS Feb_Revenue, 
SUM(Mar_Revenue) AS Mar_Revenue, 
SUM(Apr_Revenue) AS Apr_Revenue, 
SUM(May_Revenue) AS May_Revenue, 
SUM(Jun_Revenue) AS Jun_Revenue,
SUM(Jul_Revenue) AS Jul_Revenue, 
SUM(Aug_Revenue) AS Aug_Revenue, 
SUM(Sep_Revenue) AS Sep_Revenue, 
SUM(Oct_Revenue) AS Oct_Revenue, 
SUM(Nov_Revenue) AS Nov_Revenue, 
SUM(Dec_Revenue) AS Dec_Revenue
FROM new_table
GROUP BY id
