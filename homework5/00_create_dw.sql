DROP TABLE IF EXISTS fact_grades;
DROP TABLE IF EXISTS dim_student;
DROP TABLE IF EXISTS dim_teacher;
DROP TABLE IF EXISTS dim_subject;
DROP TABLE IF EXISTS dim_date;

-- date (When?)
CREATE TABLE dim_date (
    date_sk SERIAL PRIMARY KEY,
    source_date_id DATE,
    year INT,
    month INT,
    day INT,
    semester VARCHAR(10),
    is_exam_period BOOLEAN
);

-- student (Who studies?)
CREATE TABLE dim_student (
    student_sk SERIAL PRIMARY KEY,
    source_student_id INT,
    full_name VARCHAR(100),
    study_group VARCHAR(20),
    university VARCHAR(100),
    enrollment_year INT,
    city VARCHAR(50)
);

-- teacher (Who teaches?)
CREATE TABLE dim_teacher (
    teacher_sk SERIAL PRIMARY KEY,
    teacher_full_name VARCHAR(100),
    teacher_degree VARCHAR(50),
    teacher_title VARCHAR(50)
);

-- subject (What is taught?)
CREATE TABLE dim_subject (
    subject_sk SERIAL PRIMARY KEY,
    source_subject_id INT,
    subject_name VARCHAR(100),
    subject_area VARCHAR(50)
);

-- one exam attempt (center of the star)
CREATE TABLE fact_grades (
    grade_sk SERIAL PRIMARY KEY,
    date_sk INT REFERENCES dim_date(date_sk),
    student_sk INT REFERENCES dim_student(student_sk),
    teacher_sk INT REFERENCES dim_teacher(teacher_sk),
    subject_sk INT REFERENCES dim_subject(subject_sk),
    score INT,
    ects_credits INT
);

CREATE INDEX idx_fact_grades_keys
    ON fact_grades (date_sk, student_sk, teacher_sk, subject_sk);


INSERT INTO dim_date
(source_date_id, year, month, day, semester, is_exam_period) VALUES
('2024-01-15', 2024, 1, 15, 'autumn', true),
('2024-01-20', 2024, 1, 20, 'autumn', true),
('2024-06-10', 2024, 6, 10, 'spring', true),
('2024-06-25', 2024, 6, 25, 'spring', true),
('2025-01-12', 2025, 1, 12, 'autumn', true),
('2025-01-18', 2025, 1, 18, 'autumn', true),
('2025-06-09', 2025, 6, 9, 'spring', true),
('2025-06-20', 2025, 6, 20, 'spring', true);

INSERT INTO dim_student
(source_student_id, full_name, study_group, university, enrollment_year, city) VALUES
(1, 'Alexander Kovalyov', 'PA-21', 'BSU', 2021, 'Minsk'),
(2, 'Ekaterina Smirnova', 'PA-21', 'GSU', 2021, 'Gomel'),
(3, 'Dmitry Sidorov', 'IT-22', 'BNTU', 2022, 'Minsk'),
(4, 'Anastasia Kozlova', 'IT-22', 'BNTU', 2022, 'Minsk'),
(5, 'Pavel Novitsky', 'DA-23', 'BSUIR', 2023, 'Minsk');

INSERT INTO dim_teacher
(teacher_full_name, teacher_degree, teacher_title) VALUES
('Sergei Ivanov', 'PhD', 'Associate Professor'),
('Elena Vasilieva', 'PhD', 'Professor'),
('Mikhail Kuznetsov', 'None', 'Lecturer');

INSERT INTO dim_subject
(source_subject_id, subject_name, subject_area) VALUES
(1, 'Database Systems', 'CS'),
(2, 'Mathematical Analysis', 'Math'),
(3, 'Python Programming', 'CS'),
(4, 'Operating Systems', 'CS');

INSERT INTO fact_grades
(date_sk, student_sk, teacher_sk, subject_sk, score, ects_credits) VALUES
(1, 1, 1, 1, 9, 5),
(1, 2, 1, 1, 7, 5),
(1, 5, 1, 1, 5, 5),
(2, 1, 3, 3, 10, 3),
(2, 3, 3, 3, 9, 3),
(2, 4, 3, 3, 4, 3),
(3, 4, 3, 3, 7, 3),
(4, 1, 2, 2, 8, 6),
(4, 2, 2, 2, 9, 6),
(5, 3, 2, 2, 7, 6),
(5, 5, 2, 2, 5, 6),
(6, 5, 2, 2, 6, 6),
(7, 3, 1, 4, 8, 5),
(7, 4, 1, 4, 9, 5),
(7, 2, 1, 4, 7, 5),
(8, 5, 3, 3, 8, 3);