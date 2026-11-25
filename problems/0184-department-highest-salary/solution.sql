# Write your MySQL query statement below
WITH cte AS (
        SELECT
        departmentId,
        MAX(salary) AS salary_max 
    FROM Employee
    GROUP BY departmentId)

SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary

FROM Employee e

JOIN Department d
ON e.departmentId = d.id

JOIN cte
ON cte.departmentId = d.id

WHERE cte.departmentId = d.id AND cte.salary_max = e.salary
