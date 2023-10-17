-- list all records of second_table in my MySQL server.
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
