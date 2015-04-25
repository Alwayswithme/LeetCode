--
-- Author     :  Ye Jinchang
-- Date       :  2015-04-24 16:00:26
-- Title      :  178 rank scores
--

/**********************************************************************************

 Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

For example, given the above Scores table, your query should generate the following report (order by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+

*********************************************************************************/

-- Write your MySQL query statement below
SELECT s.Score,count(r.Score) AS RANK FROM 
Scores s, (SELECT DISTINCT Score FROM Scores ) r 
WHERE s.Score <= r.Score 
GROUP BY s.id 
ORDER BY s.Score DESC;
