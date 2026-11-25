# 610. Triangle Judgement

**Difficulty:** Easy  
**Topics:** Database  
**Link:** https://leetcode.com/problems/triangle-judgement/

## Statement

Table: `Triangle`

```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
```

Report for every three line segments whether they can form a triangle.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```text
Input: 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+
```

*Problem statement and examples belong to LeetCode. Kept here for personal study only.*
