# Student Report Card Management System

This project implements a Student Report Card Management System that allows administrators to manage student records, subjects, and marks. It provides an interface to add, update, delete student records, create and assign subjects to students, and manage marks. The system also generates detailed reports for individual students based on their academic performance.

## Features

### 1. **Admin Panel**
   - **Add Student Records**: Allows administrators to add new student information, including student ID, name, date of birth, and gender.
   - **Update Student Records**: Enables administrators to modify existing student details.
   - **Delete Student Records**: Allows administrators to delete a student record by providing the student ID.
   - **Create Subject**: Administrators can create new subjects, assigning a unique subject ID, name, teacher, and credit hours.
   - **Assign Subjects to Students**: Subjects can be assigned to students, initializing the marks as 0.

### 2. **Marks Management**
   - **Enter Marks for a Student**: Administrators can enter or update the marks for a student in any of their assigned subjects.
   - **View Marks for a Student**: Displays all marks obtained by a student across different subjects.

### 3. **Reports**
   - **Generate Report for a Student**: Provides a detailed report for a student, including personal information, subjects enrolled, marks obtained, total marks, average marks, and grade (A, B, C, D based on performance).

### 4. **Database Integration**
   - The system interacts with a MySQL database where student information, subject details, and marks are stored. The database consists of the following tables:
     - **students**: Stores student details such as ID, name, date of birth, and gender.
     - **subjects**: Stores subject-related information such as subject ID, name, teacher, and credit hours.
     - **marks**: Stores the marks obtained by students for each subject.

## Prerequisites

To run this project, you need to have the following installed on your machine:
- Python 3.x
- MySQL Database (with a database named `StudentReportCard`)
- `mysql-connector-python` package installed. You can install it using:
  ```bash
  pip install mysql-connector-python
  ```

## Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/student-report-card.git
   ```

2. Create a MySQL database and tables by running the following SQL script:

```sql
CREATE DATABASE StudentReportCard;

USE StudentReportCard;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    gender ENUM('Male', 'Female')
);

CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(100),
    teacher_name VARCHAR(100),
    credit_hours INT
);

CREATE TABLE marks (
    student_id INT,
    subject_id INT,
    marks_obtained INT,
    PRIMARY KEY (student_id, subject_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);
```

3. Update the MySQL connection details (`user`, `password`, and `host`) in the script to match your MySQL configuration.

## How to Use

1. **Start the System**: Run the Python script to start the Student Report Card Management System.
   ```bash
   python student_report_card.py
   ```

2. **Admin Panel**: Use the admin panel to manage student records, subjects, and assign subjects to students.

3. **Marks Management**: Enter or view marks for students in the `Marks Management` section.

4. **Reports**: Generate detailed student reports by selecting the `Reports` section.

## Code Description

- **Database Connection**: The system connects to a MySQL database using the `mysql.connector` library to execute SQL queries and interact with the database.
- **Admin Panel**: Provides options to manage students and subjects, such as adding, updating, and deleting records.
- **Marks Management**: Enables entering and viewing marks for students in specific subjects.
- **Reports Generation**: Retrieves a student's personal and academic details to generate a performance report.

## Contributing

We welcome contributions! If you have any suggestions or improvements, feel free to fork the repository and submit a pull request.



