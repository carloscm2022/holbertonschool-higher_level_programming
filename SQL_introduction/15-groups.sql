-- script that lists the number of records with the same score in the table second_tabl.
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
