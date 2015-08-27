--
-- Author     :  Ye Jinchang
-- Date       :  2015-04-26 15:17:59
-- Title      :  181 employees earning more than their managers
--
--
 
 /**********************************************************

 The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+

****************************************************************/

-- Write your MySQL query statement below
SELECT e1.Name AS Employee From Employee e1 JOIN Employee e2 ON e1.ManagerId = e2.Id WHERE e1.Salary > e2.Salary;
