--
-- Author     :  Ye Jinchang
-- Date       :  2015-04-24 16:00:25
-- Title      :  177 nth highest salary
--
 
/***************************************************************

 Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

***************************************************************/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee Emp1 WHERE (N-1) = (SELECT COUNT(DISTINCT(Salary)) 
                        FROM Employee Emp2 WHERE Emp2.Salary > Emp1.Salary)
  );
END
