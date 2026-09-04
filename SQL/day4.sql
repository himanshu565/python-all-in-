-- Q1 Write a query to find list of patients first_name, last_name, and allergies where allergies are not null and are from the city of 'Hamilton'
SELECT
  first_name,
  last_name,
  allergies
FROM patients
WHERE
  city = 'Hamilton'
  and allergies is not null

-- Q2 Show unique birth years from patients and order them by ascending.

SELECT
  DISTINCT YEAR(birth_date) AS birth_year
FROM patients
ORDER BY birth_year;
-- //Yes, GROUP BY produces a result set with distinct rows based on the columns specified in the grouping clause. 

SELECT year(birth_date)
FROM patients
GROUP BY year(birth_date)

-- Show first name, last name, and gender of patients whose gender is 'M'
SELECT
  first_name,
  last_name,
  gender
FROM patients
WHERE gender = 'M';


-- Q4 how unique first names from the patients table which only occurs once in the list.
SELECT first_name
FROM patients
GROUP BY first_name
HAVING COUNT(first_name) = 1

-- Q5 Show patient_id and first_name from patients where their first_name start and ends with 's' and is at least 6 characters long.
SELECT
  patient_id,
  first_name
FROM patients
WHERE first_name LIKE 's____%s';
/*
-- q5 Show first name of patients that start with the letter 'C'
SELECT
  first_name
FROM
  patients
WHERE
  first_name LIKE 'C%'