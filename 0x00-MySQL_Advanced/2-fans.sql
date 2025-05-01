-- Script that creates a table user
-- with id, email, name and country(enum with US, CO and TN)
CREATE TABLE IF NOT EXISTS user(
	id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);	
