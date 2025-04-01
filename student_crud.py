import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres.vpylacezgeycdtjiysys"
DB_HOST = "aws-0-ap-southeast-1.pooler.supabase.com"
DB_PORT = "6543"
DB_PASSWORD = "samrat@123#"

import psycopg2

# Database connection details
DB_NAME = "postgres"
DB_USER = "postgres.vpylacezgeycdtjiysys"
DB_HOST = "aws-0-ap-southeast-1.pooler.supabase.com"
DB_PORT = "6543"
DB_PASSWORD = "samrat@123#"

# Function to establish a connection to the database
def db_connection():
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        print("Connected to the database")
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None

# Function to drop existing tables and recreate them
def create_tables():
    conn = db_connection()
    cursor = conn.cursor()
    
    # Dropping existing tables
    cursor.execute("DROP TABLE IF EXISTS enrollments;")
    cursor.execute("DROP TABLE IF EXISTS courses;")
    cursor.execute("DROP TABLE IF EXISTS departments;")
    cursor.execute("DROP TABLE IF EXISTS student;")

    # Creating tables
    cursor.execute("""
        CREATE TABLE student (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age INT NOT NULL,
            gender VARCHAR(6) CHECK (gender IN ('MALE', 'FEMALE', 'OTHER')) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            enrollment_date DATE NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE departments (
            department_id SERIAL PRIMARY KEY,
            department_name VARCHAR(100) NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE courses (
            course_id SERIAL PRIMARY KEY,
            courses_name VARCHAR(100) NOT NULL,
            department_id INT NOT NULL,
            credits INT NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE enrollments (
            enrollment_id SERIAL PRIMARY KEY,
            student_id INT REFERENCES student (student_id) ON DELETE CASCADE,
            course_id INT REFERENCES courses (course_id) ON DELETE CASCADE,
            grade VARCHAR(2)
        );
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created successfully")

# Function to insert data into tables
def insert_data():
    conn = db_connection()
    cursor = conn.cursor()

    # Insert data into departments
    cursor.execute("""
        INSERT INTO departments (department_name) VALUES
        ('Computer Science'),
        ('Mathematics'),
        ('Physics'),
        ('Biology'),
        ('History');
    """)

    # Insert data into students
    cursor.execute("""
        INSERT INTO student (name, age, gender, email, enrollment_date) VALUES
        ('Alice Smith', 20, 'FEMALE', 'alice.smith@example.com', '2023-09-01'),
        ('Bob Johnson', 22, 'MALE', 'bob.johnson@example.com', '2023-09-01'),
        ('Charlie Brown', 19, 'MALE', 'charlie.brown@example.com', '2023-09-01'),
        ('Diana Prince', 21, 'FEMALE', 'diana.prince@example.com', '2023-09-01'),
        ('Eve Adams', 23, 'OTHER', 'eve.adams@example.com', '2023-09-01');
    """)

    # Insert data into courses
    cursor.execute("""
        INSERT INTO courses (courses_name, department_id, credits) VALUES
        ('Introduction to Programming', 1, 3),
        ('Calculus I', 2, 4),
        ('Physics Mechanics', 3, 3),
        ('Biology Basics', 4, 4),
        ('World History', 5, 3);
    """)

    # Insert data into enrollments
    cursor.execute("""
        INSERT INTO enrollments (student_id, course_id, grade) VALUES
        (1, 1, 'A'),
        (2, 2, 'B'),
        (3, 3, 'A'),
        (4, 4, 'C'),
        (5, 5, 'B');
    """)

    # Insert one more student (Frank Miller)
    cursor.execute("""
        INSERT INTO student (name, age, gender, email, enrollment_date)
        VALUES ('Frank Miller', 20, 'MALE', 'frank.miller@example.com', '2023-10-01');
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted successfully")


def add_foreign_keys():
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        ALTER TABLE departments
        ADD teacher_id INT REFERENCES teacher(teacher_id) ON DELETE CASCADE;
    """)

    # Add course_id column and foreign key constraint to departments table
    cursor.execute("""
        ALTER TABLE departments
        ADD course_id INT REFERENCES courses(course_id) ON DELETE CASCADE;
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Foreign keys added successfully")


def update_teachers(name,  age, teacher_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE teacher SET name = %s, age = %s WHERE teacher_id = %s", (name, age, id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data updated")

#def delete_teachers(name):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teacher WHERE name = %s", (name,))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Data deleted for {name}")


def teachers_data():
    return [
        ("Samrat", 17, 1),
        ("Ram", 25, 2),
        ("Shyam", 22, 3),
        ("Rita", 30, 4),
        ("Sita", 33, 5)
    ]

if __name__ == "__main__":
    # create_tables()
    
    teachers = teachers_data()
    # insert_teachers(teachers)
    # update_teachers("Ram", 26, 1)  
    #delete_teachers("Shyam") 
    #add_foreign_keys()
 
# asfdasdf
