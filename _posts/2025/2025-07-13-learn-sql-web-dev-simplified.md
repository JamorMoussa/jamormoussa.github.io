---
author: owner
title: Learn SQL - Web Dev Simplified
date: 2025-07-13
categories: [Programming Language, SQL]
tags: []  # TAG names should always be lowercase
description: # add some description here
math: true  # optional

image:
  path: "assets/headers/learn-sql-web.png"
---


# Learn SQL - Web Dev Simplified

**SQL** (*Structured Query Language*) is a standard language for interacting with relational databases. Below is a quick summary based on the [Web Dev Simplified SQL tutorial](https://www.youtube.com/watch?v=p3qvj9hO_Bo), with short explanations before each code section.

## 📘 Create & Select a Database

Basic commands to create a database, delete it, and switch context to it.

```sql
-- Create a new database
CREATE DATABASE testdb;

-- Delete a database (⚠️ irreversible)
DROP DATABASE testdb;

-- Set the active database
USE testdb;
```

## 🧱 Creating Tables

Define tables for storing band and album information, including data types and relationships.

```sql
-- Create a new database for records
CREATE DATABASE record_company;

-- Create a table for bands
CREATE TABLE bands (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

-- Add a new column to the bands table
ALTER TABLE bands 
ADD added_col VARCHAR(255);  -- Adds an extra column to the table
```

```sql
-- Create albums table with a foreign key to bands
CREATE TABLE albums (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    release_year INT,
    band_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (band_id) REFERENCES bands(id)
);
```

## ✍️ Insert & Query Data

Insert data into tables and retrieve it using basic `SELECT` queries.

```sql
-- Insert one band into the bands table
INSERT INTO bands (name)
VALUES ('Iron Maiden');

-- Insert multiple bands at once
INSERT INTO bands (name)
VALUES ('Deuce'), ('Avenged Sevenfold'), ('Ankor');
```

```sql
-- Show all rows in bands
SELECT * FROM bands;

-- Show only the first two records
SELECT * FROM bands LIMIT 2;

-- Select with aliasing for better output
SELECT id AS 'ID', name AS 'Band Name'
FROM bands;

-- Sort results alphabetically in descending order
SELECT * FROM bands ORDER BY name DESC;
```

```sql
-- Insert multiple albums linked to bands by band_id
INSERT INTO albums (name, release_year, band_id)
VALUES 
  ('The Number of the Beasts', 1985, 1),
  ('Power Slave', 1984, 1),
  ('Nightmare', 2018, 2),
  ('Nightmare', 2010, 3),
  ('Test Album', NULL, 3);
```

## 🔎 Filtering Data

Use various `WHERE` filters to narrow down query results.

```sql
-- Show unique album names only
SELECT DISTINCT name FROM albums;

-- Update the release year of an album
UPDATE albums
SET release_year = 1982
WHERE id = 1;
```

```sql
-- Get albums released before 2000
SELECT * FROM albums
WHERE release_year < 2000;

-- Filter by string pattern or band ID
SELECT * FROM albums
WHERE name LIKE '%er%' OR band_id = 2;
```

```sql
-- Filter albums released between two years
SELECT * FROM albums
WHERE release_year BETWEEN 2000 AND 2019;

-- Select albums with unknown (NULL) release years
SELECT * FROM albums
WHERE release_year IS NULL;

-- Delete albums where the release year is NULL
DELETE FROM albums
WHERE release_year IS NULL;
```

## 🔗 Joining Tables

Combine data from `bands` and `albums` using JOIN operations.

```sql
-- Inner join to match albums with their bands
SELECT * FROM bands
JOIN albums ON bands.id = albums.band_id;

-- Note:
-- INNER JOIN = only matching records
-- LEFT JOIN = all bands even if they have no albums
-- RIGHT JOIN = all albums even if the band is missing
```

## 📊 Aggregation & Grouping

Use aggregation functions like `AVG`, `COUNT`, and `GROUP BY` to summarize data.

```sql
-- Calculate average release year of all albums
SELECT AVG(release_year) FROM albums;

-- Count how many albums each band has
SELECT band_id, COUNT(band_id) FROM albums
GROUP BY band_id;
```

```sql
-- Count albums per band and show the band name
SELECT 
  b.name AS band_name, 
  COUNT(a.id) AS num_albums
FROM bands AS b
LEFT JOIN albums AS a ON a.band_id = b.id
GROUP BY a.band_id
HAVING num_albums >= 1;

-- Use HAVING (not WHERE) after GROUP BY to filter results
```

This guide gives you hands-on SQL practice for basic data modeling, querying, and relational operations—perfect for learning the foundations of relational databases.


## Exercices:


1. Create a Songs Table 

    ```sql
    CREATE TABLE songs (
      id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        length INT NOT NULL,
        album_id INT NOT NULL, 
        PRIMARY KEY (id),
        FOREIGN KEY (album_id) REFERENCES albums(id)
    );
    ```

2. Select only the Names of all the Bands
    
    ```sql
    SELECT name as "Band Name" FROM bands;
    ```

    | Band Name         | 
    |-------------------| 
    | Seventh Wonder    | 
    | Metallica         | 
    | The Ocean         | 
    | Within Temptation | 
    | Death             | 
    | Van Canto         | 
    | Dream Theater     | 

3. Select the Oldest Album

    ```sql
    SELECT * FROM albums
    WHERE release_year IS NOT NULL
    ORDER BY release_year ASC LIMIT 1;
    ```

    | id | name                   | release_year | band_id | 
    |----|------------------------|--------------|---------| 
    | 5  | ...And Justice for All | 1988         | 2       | 

4. Get all Bands that have Albums

    ```sql
    SELECT DISTINCT b.name as 'Band Name' FROM bands as b 
    JOIN albums as a ON a.band_id = b.id;
    ```

    | Band Name         | 
    |-------------------| 
    | Seventh Wonder    | 
    | Metallica         | 
    | The Ocean         | 
    | Within Temptation | 
    | Death             | 
    | Van Canto         | 

5. Get all Bands that have No Albums

    ```sql
    SELECT DISTINCT b.name as 'Band Name' FROM bands as b 
    LEFT OUTER JOIN albums as a ON a.band_id = b.id
    WHERE a.id IS NULL;
    ```

    | Band Name     | 
    |---------------| 
    | Dream Theater | 

6. Get the Longest Album

    ```sql
    SELECT 
      a.name, 
      a.release_year, 	
      SUM(s.length) AS length 
    FROM albums AS a 
    JOIN songs AS s ON a.id = s.album_id
    GROUP BY a.name, a.release_year
    ORDER BY length DESC LIMIT 1;
    ```

    | Name           | Release Year | Duration          | 
    |----------------|--------------|-------------------| 
    | Death Magnetic | 2008         | 74.76666593551636 | 

7. Update the Release Year of the Album with no Release Year

    ```sql
    UPDATE albums
    SET release_year = 1986
    WHERE release_year IS NULL;
    ```

8. Insert a record for your favorite Band and one of their Albums

    ```sql
    INSERT INTO bands (name)
    VALUES ('Favorite Band Name');

    INSERT INTO albums (name, release_year, band_id)
    VALUES ('Favorite Album Name', 2000, 8);
    ```

9. Delete the Band and Album you added in #8

    ```sql
    DELETE FROM albums
    WHERE id = 8;

    DELETE FROM bands
    WHERE id = 8;
    ```

10. Get the Average Length of all Songs

    ```sql
    SELECT AVG(length) as "Average Song Duration" FROM songs; 
    ```

    | Average Song Duration | 
    |-----------------------| 
    | 5.352472513259112     | 

11. Select the longest Song off each Album

    ```sql
    SELECT 
      a.name AS "Album",
        a.release_year AS "Release Year",
        MAX(s.length) AS "Duration"
    FROM albums AS a 
    JOIN songs AS s ON a.id = s.album_id
    GROUP BY a.name, a.release_year;
    ```

    | Album                       | Release Year | Duration | 
    |-----------------------------|--------------|----------| 
    | Tiara                       | 2018         | 9.5      | 
    | The Great Escape            | 2010         | 30.2333  | 
    | Mercy Falls                 | 2008         | 9.48333  | 
    | Master of Puppets           | 1986         | 8.58333  | 
    | ...And Justice for All      | 1988         | 9.81667  | 
    | Death Magnetic              | 2008         | 9.96667  | 
    | Heliocentric                | 2010         | 7.48333  | 
    | Pelagial                    | 2013         | 9.28333  | 
    | Anthropocentric             | 2010         | 9.4      | 
    | Resist                      | 2018         | 5.85     | 
    | The Unforgiving             | 2011         | 5.66667  | 
    | Enter                       | 1997         | 7.25     | 
    | The Sound of Perseverance   | 1998         | 8.43333  | 
    | Individual Thought Patterns | 1993         | 4.81667  | 
    | Human                       | 1991         | 4.65     | 
    | A Storm to Come             | 2006         | 5.21667  | 
    | Break the Silence           | 2011         | 6.15     | 
    | Tribe of Force              | 2010         | 8.38333  | 

12. Get the number of Songs for each Band

    ```sql
    SELECT
      b.name AS "Band",
      COUNT(s.name) AS "Number of Songs"
    FROM bands as b
    JOIN albums as a ON b.id = a.band_id
    JOIN songs as s ON a.id = s.album_id
    GROUP BY b.name;
    ```

    | Band              | Number of Songs | 
    |-------------------|-----------------| 
    | Seventh Wonder    | 35              | 
    | Metallica         | 27              | 
    | The Ocean         | 31              | 
    | Within Temptation | 30              | 
    | Death             | 27              | 
    | Van Canto         | 32              | 

## Todo: 

- Add shema of database
- Add section about joins type: [https://medium.com/@authfy/seven-join-techniques-in-sql-a65786a40ed3](https://medium.com/@authfy/seven-join-techniques-in-sql-a65786a40ed3)