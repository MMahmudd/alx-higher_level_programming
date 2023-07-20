-- lists_all cities_contained in_the database_hbtn_0d_usa.

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
