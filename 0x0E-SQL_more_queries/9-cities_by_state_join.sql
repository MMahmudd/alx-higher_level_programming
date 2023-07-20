-- Query: List all cities from the database hbtn_0d_usa.
-- Each record should display: City ID, City Name, and State Name.
-- Results must be sorted in ascending order by City ID.
-- The database name "hbtn_0d_usa" will be passed as an argument of the mysql command.

SELECT cities.id AS 'City ID', cities.name AS 'City Name', states.name AS 'State Name'
FROM hbtn_0d_usa.cities
JOIN hbtn_0d_usa.states ON cities.state_id = states.id
ORDER BY cities.id;
