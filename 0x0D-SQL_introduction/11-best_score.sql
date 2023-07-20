-- lists all_records with_a_score >= 10 in_the table_second_table of_the_database hbtn_0c_0 in_my_MySQL server

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
