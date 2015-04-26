--
-- Author     :  Ye Jinchang
-- Date       :  2015-04-24 16:00:27
-- Title      :  180 consecutive numbers
--

/*****************************************************************

  Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+

For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

*****************************************************************/

-- Write your MySQL query statement below
SELECT DISTINCT Num FROM 
  (SELECT Num, IF(Num = @last, @row := @row + 1, @row := 1) as times, @last := Num FROM Logs, 
    (SELECT @last := 'x', @row := 0) r
  ) t
WHERE times >= 3
