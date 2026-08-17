-- Q1 Show how many patients have a birth_date with 2010 as the birth year.

SELECT COUNT(*) AS total_patients
FROM patients
WHERE YEAR(birth_date) = 2010;

-- Q2 Show the first_name, last_name, and height of the patient with the greatest height.

SELECT
  first_name,
  last_name,
  height
FROM patients
WHERE height = (
    SELECT max(height)
    FROM patients
  )