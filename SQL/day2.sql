-- Q1. Show first name and last name concatinated into one column to show their full name.

SELECT
  CONCAT(first_name, ' ', last_name) AS full_name
FROM patients;

-- method 2 
SELECT
  CONCAT(first_name, ' ', last_name) AS full_name
FROM patients;

SELECT first_name || ' ' || last_name
FROM patients;

-- Q2. Show first name, last name, and the full province name of each patient.

-- Example: 'Ontario' instead of 'ON'
SELECT
  first_name,
  last_name,
  province_name
FROM patients
  JOIN province_names ON province_names.province_id = patients.province_id;