-- Display all cities in the database using JOIN
-- statement to do join query
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC;
