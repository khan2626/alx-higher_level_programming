-- Creates table unique_id on my MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1,
UNIQUE (id),
name VARCHAR(256));
