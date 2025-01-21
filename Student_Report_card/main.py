import mysql.connector

connection = mysql.connector.connect(
    user="root",
    password="Lakshya@123",
    host="localhost",
    database="StudentReportCard"
)
cursor = connection.cursor()

def admin_panel():
    while True:
        print('''
1. Add Student Records      
2. Update Student Records   
3. Delete Student Records  
4. Create Subject  
5. Assign Subjects to Students   
6. Logout   
              ''')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student_report()
        elif choice == 2:
            update_student_report()
        elif choice == 3:
            delete_student_report()
        elif choice == 4:
            create_subject()
        elif choice == 5:
            assign_subject_to_student()
        elif choice == 6:
            break
        else:
            print("Invalid choice..... Try again.")

def add_student_report():
    try:
        student_id = int(input("Enter the Student ID: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        dob = input("Enter DOB (YYYY-MM-DD): ")
        gender = input("Enter Gender (Male/Female): ")

        query = '''
        INSERT INTO students 
        (student_id, first_name, last_name, date_of_birth, gender)
        VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (student_id, first_name, last_name, dob, gender))
        connection.commit()  # Commit the transaction to the database

        print("Student added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def update_student_report():
    try:
        student_id = int(input("Enter the Student ID to update: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        dob = input("Enter DOB (YYYY-MM-DD): ")
        gender = input("Enter Gender (Male/Female): ")

        query = '''
        UPDATE students
        SET first_name = %s, last_name = %s, date_of_birth = %s, gender = %s
        WHERE student_id = %s
        '''
        cursor.execute(query, (first_name, last_name, dob, gender, student_id))
        connection.commit()

        print("Student data updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def delete_student_report():
    try:
        student_id = int(input("Enter the Student ID to delete: "))
        query = '''
        DELETE FROM students
        WHERE student_id = %s
        '''
        cursor.execute(query, (student_id,))
        connection.commit()

        print("Student deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

def create_subject():
    try:
        subject_id = int(input("Enter Subject ID: "))
        subject_name = input("Enter Subject Name: ")
        teacher_name = input("Enter Teacher Name: ")
        credit_hours = int(input("Enter Credit Hours: "))

        query = '''
        INSERT INTO subjects (subject_id, subject_name, teacher_name, credit_hours)
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(query, (subject_id, subject_name, teacher_name, credit_hours))
        connection.commit()

        print("Subject created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def assign_subject_to_student():
    try:
        student_id = int(input("Enter Student ID: "))
        subject_id = int(input("Enter Subject ID: "))
        
        query = '''
        INSERT INTO marks (student_id, subject_id, marks_obtained)
        VALUES (%s, %s, 0)  -- Initial marks as 0
        '''
        cursor.execute(query, (student_id, subject_id))
        connection.commit()

        print("Subject assigned to student successfully.")
    except Exception as e:
        print(f"Error: {e}")

def marks_management():
    while True:
        print('''
1. Enter Marks for a Student
2. View Marks for a Student
3. Back to Admin Panel
        ''')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            enter_marks_for_student()
        elif choice == 2:
            view_marks_for_student()
        elif choice == 3:
            break
        else:
            print("Invalid choice, try again.")

def enter_marks_for_student():
    try:
        student_id = int(input("Enter Student ID: "))
        subject_id = int(input("Enter Subject ID: "))
        marks = int(input("Enter Marks Obtained: "))

        query = '''
        UPDATE marks
        SET marks_obtained = %s
        WHERE student_id = %s AND subject_id = %s
        '''
        cursor.execute(query, (marks, student_id, subject_id))
        connection.commit()

        print("Marks updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def view_marks_for_student():
    try:
        student_id = int(input("Enter Student ID: "))

        query = '''
        SELECT s.subject_name, m.marks_obtained
        FROM marks m
        JOIN subjects s ON m.subject_id = s.subject_id
        WHERE m.student_id = %s
        '''
        cursor.execute(query, (student_id,))
        results = cursor.fetchall()

        if results:
            for row in results:
                 print(f"Subject: {row[0]}, Marks: {row[1]}")
        else:
            print("No marks found for the student.")
    except Exception as e:
        print(f"Error: {e}")

def generate_report(student_id):
    try:
        query = '''
        SELECT first_name, last_name, date_of_birth, gender
        FROM students
        WHERE student_id = %s
        '''
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()

        if student:
            print(f"Name: {student[0]} {student[1]}")
            print(f"DOB: {student[2]}, Gender: {student[3]}")

            query = '''
            SELECT s.subject_name, m.marks_obtained
            FROM marks m
            JOIN subjects s ON m.subject_id = s.subject_id
            WHERE m.student_id = %s
            '''
            cursor.execute(query, (student_id,))
            marks = cursor.fetchall()

            total_marks = sum([mark[1] for mark in marks])

            total_subjects = len(marks)
            average_marks = total_marks / total_subjects if total_subjects > 0 else 0

            grade = ''
            if average_marks >= 90:
                grade = 'A'
            elif average_marks >= 75:
                grade = 'B'
            elif average_marks >= 50:
                grade = 'C'
            else:
                grade = 'D'

            print(f"Total Marks: {total_marks}, Average Marks: {average_marks}, Grade: {grade}")
        else:
            print("Student not found.")
    except Exception as e:
        print(f"Error: {e}")

def reports():
    while True:
        print('''
1. Generate Report for a Student
2. Back to Admin Panel
        ''')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            student_id = int(input("Enter Student ID: "))
            generate_report(student_id)
        elif choice == 2:
            break
        else:
            print("Invalid choice, try again.")

def start():
    while True:
        print("--------Student Report Card---------")
        print("1. Admin Panel")
        print("2. Marks Management")
        print("3. Reports")
        print("4. Exit")
        choose = int(input("Enter your choice: "))

        if choose == 1:
            admin_panel()
        elif choose == 2:
            marks_management()
        elif choose == 3:
            reports()
        elif choose == 4:
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    start()
