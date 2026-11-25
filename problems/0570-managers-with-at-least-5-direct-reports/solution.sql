# Write your MySQL query statement below
WITH reports_count AS (SELECT name, managerId, COUNT(managerId) as reports FROM Employee GROUP BY managerId)
SELECT Employee.name
FROM Employee
JOIN reports_count
ON reports_count.managerId = Employee.Id
WHERE reports_count.reports >= 5
