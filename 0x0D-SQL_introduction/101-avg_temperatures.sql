-- displays_the_average_temperature by_city ordered_by temperature_descending.

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
