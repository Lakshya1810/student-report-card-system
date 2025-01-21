CREATE DATABASE IF NOT EXISTS StudentReportCard;
USE StudentReportCard;
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    gender ENUM('Male', 'Female')
);
CREATE TABLE IF NOT EXISTS subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(100),
    teacher_name VARCHAR(100),
    credit_hours INT
);
CREATE TABLE IF NOT EXISTS marks (
    student_id INT,
    subject_id INT,
    marks_obtained INT DEFAULT 0,
    PRIMARY KEY (student_id, subject_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
        ON DELETE CASCADE
);
select * from students;
select * from subjects;
select * from marks;
drop table students;
drop table subjects;
drop table marks;
