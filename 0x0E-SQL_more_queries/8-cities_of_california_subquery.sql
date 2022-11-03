-- List all the cities of California found int the database
-- DML query to get all cities in California (state_id = 1)
SELECT id,name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;

