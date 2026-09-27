
-- Q1  Display every patient's first_name.
-- Order the list by the length of each name and then by alphabetically

SELECT first_name
FROM patients
order by
  len(first_name),
  first_name;

--   Q2 Show the total amount of male patients and the total amount of female patients in the patients table.
-- Display the two results in the same row.
SELECT 
  (SELECT count(*) FROM patients WHERE gender='M') AS male_count, 
  (SELECT count(*) FROM patients WHERE gender='F') AS female_count;