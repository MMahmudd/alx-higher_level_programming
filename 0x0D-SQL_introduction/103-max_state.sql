-- display the_max_temperature of_each_state ordered_by_State_name.

SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
