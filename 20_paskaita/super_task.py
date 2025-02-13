import sqlite3

def create_database():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    grade INTEGER,
                    average REAL
            )''')
    c.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    subject TEXT NOT NULL
            )''')

    conn.commit()
    conn.close()

class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Student(Person):
    def __init__(self, name, surname, grade=None, average=None):
        super().__init__(name, surname)
        self.grade = grade
        self.average = average

class Teacher(Person):
    def __init__(self, name, surname, subject):
        super().__init__(name, surname)
        self.subject = subject

def log_operation(func):
    def wrapper(*args, **kwargs):
        print("Ongoing operation...")
        return func(*args, **kwargs)
    return wrapper

@log_operation
def insert_student(student):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('INSERT INTO students (name, surname, grade, average) VALUES (?, ?, ?, ?)',(student.name, student.surname, student.grade, student.average))
    conn.commit()
    conn.close()

@log_operation
def insert_teacher(teacher):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('INSERT INTO teachers (name, surname, subject) VALUES (?, ?, ?)', (teacher.name, teacher.surname, teacher.subject))
    conn.commit()
    conn.close()

@log_operation
def update_student_by_id(student_id, new_grade):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('UPDATE students SET grade = ? WHERE id = ?', (new_grade, student_id))
    conn.commit()
    conn.close()

@log_operation
def update_teacher(teacher_id, new_subject):
    conn = sqlite3.connect('school.db')
    c = conn. cursor()
    c.execute('UPDATE teachers SET subject = ? WHERE id = ?', (new_subject, teacher_id))
    conn.commit()
    conn.close()

@log_operation
def delete_student(student_id):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()

@log_operation
def delete_teacher(teachert_id):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('DELETE FROM teachers WHERE id = ?', (teachert_id,))
    conn.commit()
    conn.close()

@log_operation
def search_student(name, surname):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE name = ? AND surname = ?", (name, surname))
    result = c.fetchone()
    return result
@log_operation

def search_teacher(name, surname):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute("SELECT * FROM teachers WHERE name = ? AND surname = ?", (name, surname))
    result = c.fetchone()
    return result

@log_operation
def get_all_students():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    result = c.fetchall()
    conn.close()
    return result

class StudentIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        raise StopIteration

def show_all_students():
    students = get_all_students()
    student_iterator = StudentIterator(students)

    for student in student_iterator:
        print(student)


def add_student():
    try:
        name = input('Enter student name: ')
        surname = input('Enter student surname: ')
        grade = int(input('Enter student grade: '))
        average = float(input('Enter student average: '))
        student = Student(name, surname, grade,average)
        insert_student(student)
        print('Student added successfully!')
    except ValueError:
        print('ERROR: wrong format...')


create_database()
add_student()
show_all_students()
