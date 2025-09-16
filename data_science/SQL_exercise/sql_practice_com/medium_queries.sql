--Show unique birth years from patients and order them by ascending.
SELECT
   DISTINCT(YEAR(birth_date)) as bith_year
from patients
order by bith_year ASC;

--II
SELECT
  DISTINCT YEAR(birth_date) AS birth_year
FROM patients
ORDER BY birth_year;

--Show unique first names from the patients table which only occurs once in the list.
--For example, if two or more people are named 'John' in the first_name column then don't include their name in the output list. If only 1 person is named 'Leo' then include them in the output.
SELECT
    first_name
FROM patients
GROUP BY first_name
HAVING COUNT(*)=1;

--Show patient_id and first_name from patients where their first_name start and ends with 's' and is at least 6 characters long.
SELECT
	patient_id,
    first_name
FROM patients
WHERE first_name LIKE 's%s' AND LENGTH(first_name)>=6;


--Show patient_id, first_name, last_name from patients whos diagnosis is 'Dementia'.
--Primary diagnosis is stored in the admissions table.
SELECT
	p.patient_id,
    p.first_name,
    p.last_name
FROM patients AS p
JOIN admissions AS a ON p.patient_id=a.patient_id
WHERE a.diagnosis = 'Dementia';

--Display every patient's first_name. Order the list by the length of each name and then by alphabetically.
SELECT
   first_name
FROM patients
order by LENGTH(first_name), first_name ASC;

--Show the total amount of male patients and the total amount of female patients in the patients table.Display the two results in the same row.
SELECT
	SUM(gender='M') as male_count,
    SUM(gender='F') AS female_count
FROM patients

--
select 
  sum(case when gender = 'M' then 1 end) as male_count,
  sum(case when gender = 'F' then 1 end) as female_count 
from patients;
--

--Show first and last name, allergies from patients which have allergies to either 'Penicillin' or 'Morphine'. Show results ordered ascending by allergies then by first_name then by last_name.
SELECT 
   first_name,
   last_name,
   allergies
FROM patients
WHERE allergies IN ('Penicillin', 'Morphine')
ORDER BY allergies, first_name, last_name; 

--Show patient_id, diagnosis from admissions. Find patients admitted multiple times for the same diagnosis.
SELECT
  patient_id,
  diagnosis
FROM admissions
GROUP BY
  patient_id,
  diagnosis
HAVING Count(*) > 1;

--Show the city and the total number of patients in the city.Order from most to least patients and then by city name ascending.
SELECT
  city,
  COUNT(*) AS num_patients
FROM patients
GROUP BY city
ORDER BY num_patients DESC, city ASC;

--
SELECT first_name, last_name, 'Patient' as role FROM patients
    union all
select first_name, last_name, 'Doctor' from doctors;

--Show all allergies ordered by popularity. Remove NULL values from query.
SELECT 
  allergies,
  COUNT(*) AS total_diagnosis
FROM patients
WHERE allergies IS NOT NULL
GROUP BY allergies
ORDER BY total_diagnosis DESC;


--Show all patient's first_name, last_name, and birth_date who were born in the 1970s decade. Sort the list starting from the earliest birth_date.
SELECT
  first_name,
  last_name,
  birth_date
FROM patients
WHERE YEAR(birth_date) BETWEEN 1970 AND 1979
ORDER BY birth_date;

--We want to display each patient's full name in a single column. Their last_name in all upper letters must appear first, then first_name in all lower case letters. Separate the last_name and first_name with a comma. Order the list by the first_name in decending order EX: SMITH,jane
SELECT
  CONCAT(UPPER(last_name), ',',LOWER(first_name)) as new_name_format
from patients
order by first_name DESC;

--Show the province_id(s), sum of height; where the total sum of its patient's height is greater than or equal to 7,000.
SELECT
  pn.province_id,
  SUM(p.height) AS sum_height
FROM province_names AS pn
INNER JOIN patients as p ON pn.province_id=p.province_id
group by pn.province_id
having sum_height > 7000;

--Show the difference between the largest weight and smallest weight for patients with the last name 'Maroni'
SELECT
  (max(weight) - min(weight)) AS weight_delta
FROM patients
WHERE last_name='Maroni';

--Show all of the days of the month (1-31) and how many admission_dates occurred on that day. Sort by the day with most admissions to least admissions.
SELECT 
  DAY(admission_date) AS day_number,
  COUNT(DAY(admission_date))  AS number_of_admissions
FROM admissions
group by day_number
order by number_of_admissions DESC;

--Show all columns for patient_id 542's most recent admission_date.
SELECT
  patient_id,
  max(admission_date),
  discharge_date,
  diagnosis,
  attending_doctor_id
FROM admissions
WHERE patient_id=542 ;

--Show patient_id, attending_doctor_id, and diagnosis for admissions that match one of the two criteria:
--1. patient_id is an odd number and attending_doctor_id is either 1, 5, or 19.
--2. attending_doctor_id contains a 2 and the length of patient_id is 3 characters.
SELECT
  patient_id,
  attending_doctor_id,
  diagnosis
FROM admissions
WHERE
(
    patient_id % 2 = 1
    AND attending_doctor_id IN (1, 5, 19)
  )
  OR (
    CAST(attending_doctor_id AS TEXT) LIKE '%2%'
    AND LENGTH(CAST(patient_id AS TEXT)) = 3
  );

