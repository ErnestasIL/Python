from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///school.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    surname = Column(String)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    surname = Column(String)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

def insert_student():
    first_name = input("Enter student first name: ")
    surname = input("Enter student surname: ")
    if not session.query(Student).filter_by(surname=surname).first():
        session.add(Student(first_name=first_name, surname=surname))
        session.commit()
        print("Student added successfully!")
    else:
        print("Student already exists!")


def insert_teacher():
    first_name = input("Enter teacher first name: ")
    surname = input("Enter teacher surname: ")
    if not session.query(Teacher).filter_by(surname=surname).first():
        session.add(Teacher(first_name=first_name, surname=surname))
        session.commit()
        print("Teacher added successfully!")
    else:
        print("Teacher already exists!")


def get_all_students():
    students = session.query(Student).all()
    for student in students:
        print(student.id, student.first_name, student.surname)


def get_all_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(teacher.id, teacher.first_name, teacher.surname)


while True:
    print("\n1. Add Student")
    print("2. Add Teacher")
    print("3. View All Students")
    print("4. View All Teachers")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        insert_student()
    elif choice == '2':
        insert_teacher()
    elif choice == '3':
        get_all_students()
    elif choice == '4':
        get_all_teachers()
    elif choice == '5':
        break
    else:
        print("Invalid choice, try again.")

