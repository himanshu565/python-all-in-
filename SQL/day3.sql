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

-- Q3 Show all columns for patients who have one of the following patient_ids:
-- 1,45,534,879,1000
SELECT *
FROM patients
WHERE
  patient_id IN (1, 45, 534, 879, 1000);

-- Q4 Show the total number of admissions
SELECT count(patient_id) as total_patients from admissions

-- Q5 Show the patient id and the total number of admissions for patient_id 579.
SELECT
  patient_id,
  COUNT(*) AS total_admissions
FROM admissions
WHERE patient_id = 579;