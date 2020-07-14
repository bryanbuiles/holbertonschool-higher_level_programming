-- lists all the cities of California that can be found in the database
SELECT cities.id, cities.name
FROM cities, states
WHERE state.name = 'California' AND cities.state_id = states.id
ORDER BY cities.id ASC;
