--
-- Author     :  Ye Jinchang
-- Date       :  2015-04-24 16:00:17
-- Title      :  176 second highest salary
--


/*****************************************************************************

  Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the second highest salary is 200. If there is no second highest salary, then the query should return null.

*****************************************************************************/


-- Write your MySQL query statement below
SELECT MAX(Salary) as SecondHighestSalary FROM Employee WHERE Salary <> (SELECT MAX(Salary) FROM Employee);
