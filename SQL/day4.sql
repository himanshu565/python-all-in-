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
