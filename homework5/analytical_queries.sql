-- Analytical queries 

-- Q1. Which subjects are the hardest for students?
SELECT
    dim_subject.subject_name,
    ROUND(AVG(fact_grades.score), 2) AS avg_score,
    COUNT(*) AS attempts
FROM
    fact_grades
JOIN dim_subject
    ON dim_subject.subject_sk = fact_grades.subject_sk
GROUP BY
    dim_subject.subject_name
ORDER BY
    avg_score;

-- Q2. How does academic performance change over years and semesters?
SELECT
    dim_date.year,
    dim_date.semester,
    ROUND(AVG(fact_grades.score), 2) AS avg_score
FROM
    fact_grades
JOIN dim_date
    ON dim_date.date_sk = fact_grades.date_sk
GROUP BY
    dim_date.year,
    dim_date.semester
ORDER BY
    dim_date.year,
    dim_date.semester;

-- Q3. Who are the best students by average score?
SELECT
    dim_student.full_name,
    dim_student.study_group,
    ROUND(AVG(fact_grades.score), 2) AS avg_score
FROM
    fact_grades
JOIN dim_student
    ON dim_student.student_sk = fact_grades.student_sk
GROUP BY
    dim_student.full_name,
    dim_student.study_group
ORDER BY
    avg_score DESC
LIMIT 3;

-- Q4. Which subjects require the most retakes?
WITH attempts AS (
    SELECT
        subject_sk,
        student_sk,
        ROW_NUMBER() OVER (
            PARTITION BY student_sk, subject_sk
            ORDER BY date_sk
        ) AS attempt_number
    FROM
        fact_grades
)
SELECT
    dim_subject.subject_name,
    COUNT(*) AS retakes
FROM
    attempts
JOIN dim_subject
    ON dim_subject.subject_sk = attempts.subject_sk
WHERE
    attempts.attempt_number > 1
GROUP BY
    dim_subject.subject_name
ORDER BY
    retakes DESC;

-- Q5. What is the average student result per teacher?
SELECT
    dim_teacher.teacher_full_name,
    dim_teacher.teacher_title,
    COUNT(*) AS exams,
    ROUND(AVG(fact_grades.score), 2) AS avg_score
FROM
    fact_grades
JOIN dim_teacher
    ON dim_teacher.teacher_sk = fact_grades.teacher_sk
GROUP BY
    dim_teacher.teacher_full_name,
    dim_teacher.teacher_title
ORDER BY
    avg_score DESC;