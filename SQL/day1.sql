
-- Q1 Show first name of patients that start with the letter 'C'
SELECT
  first_name
FROM
  patients
WHERE
  first_name LIKE 'C%'


-- Q2 Show first name and last name of patients that weight within the range of 100 to 120 (inclusive)

SELECT
    first_name,
    last_name
FROM 
    patients
WHERE
    weight BETWEEN 100 AND 120

-- Q3 Update the patients table for the allergies column. If the patient's allergies is null then replace it with 'NKA'

UPDATE patients
SET allergies = 'NKA'
WHERE allergies IS NULL;