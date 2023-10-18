-- Creates database hbtn_0d_usa and the table states.
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
CREATE TABLE IF NOT EXIST states (
id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL);
