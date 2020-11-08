# Write your MySQL query statement below
SELECT MIN(ABS(P1.x - P2.x)) AS shortest FROM point AS P1
JOIN point AS P2 on P1.x <> P2.x
