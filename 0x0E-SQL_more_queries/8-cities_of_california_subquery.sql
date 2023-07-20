-- Query: List all the cities of California from the database hbtn_0d_usa.
-- The states table contains only one record with the name "California".
-- The results must be sorted in ascending order by cities.id.
-- The database name (hbtn_0d_usa) will be passed as an argument of the mysql command.

SELECT id, name FROM hbtn_0d_usa.cities
WHERE state_id = (
      SELECT id FROM hbtn_0d_usa.states
      WHERE name = "California")
ORDER BY id;
