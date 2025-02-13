import sqlite3

def create_database():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER,
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
        try:
            print(f'Executing: {func.__name__}')
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Error in {func.__name__}: {e}')
    return wrapper

@log_operation
def insert_student(student):
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, surname, grade, average) VALUES (?, ?, ?, ?)',(student.name, student.surname, student.grade, student.average))

@log_operation
def insert_teacher(teacher):
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO teachers (name, surname, subject) VALUES (?, ?, ?)', (teacher.name, teacher.surname, teacher.subject))

@log_operation
def update_student_by_id(student_id, new_grade):
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE students SET grade = ? WHERE id = ?', (new_grade, student_id))

@log_operation
def update_teacher(teacher_id, new_subject):
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE teachers SET subject = ? WHERE id = ?', (new_subject, teacher_id))

@log_operation
def delete_student(student_id):
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))

@log_operation
def delete_teacher(teacher_id):
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM teachers WHERE id = ?', (teacher_id,))

@log_operation
def search_student(name, surname):
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name = ? AND surname = ?", (name, surname))
        result = cursor.fetchone()
        return result
@log_operation

def search_teacher(name, surname):
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teachers WHERE name = ? AND surname = ?", (name, surname))
        result = cursor.fetchone()
        return result

@log_operation
def get_all_students():
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        result = cursor.fetchall()
        return result

def get_all_teachers():
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM teachers')
        result = cursor.fetchall()
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
        print(f"ID: {student[0]}, Name: {student[1]}, Surname: {student[2]}, Grade: {student[3]}, Average: {student[4]}")

def show_all_teachers():
    teacher = get_all_teachers()
    teacher_iterator = StudentIterator(teacher)

    for student in teacher_iterator:
        print(student)

def add_student():
    name = input('Enter student name: ')
    surname = input('Enter student surname: ')
    while True:
        try:
            grade = int(input('Enter student grade: '))
            break
        except ValueError:
            print('ERROR: Grade must be integer')
    while True:
        try:
            average = float(input('Enter student average: '))
            break
        except ValueError:
            print('ERROR: Average must be a number')
    student = Student(name, surname, grade, average)
    insert_student(student)
    print('Student added successfully!')

def add_teacher():
    name = input('Enter teacher name: ')
    surname = input('Enter teacher surname: ')
    subject = input('Enter teacher subject: ')
    teacher = Teacher(name, surname, subject)
    insert_teacher(teacher)
    print('Teacher added successfully!')

def remove_student_by_id():
    student_id = int(input('Enter student ID to delete: '))
    delete_student(student_id)
    print('Student has been deleted')



create_database()
# add_student()
remove_student_by_id()
show_all_students()
# add_teacher()
# show_all_teachers()