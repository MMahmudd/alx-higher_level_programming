-- lists_the number_of_records with_the same_score in_the_table.

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
