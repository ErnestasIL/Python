from operator import index

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mokiniai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Mokinys(db.Model):
    __tablename__ = 'mokinys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    grade = db.Column(db.Integer)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def add_to_grade(self):
        if self.grade + 1 > 12:
            return 'Finishes school'
        else:
            return self.grade + 1

    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = surname
        self.grade = grade

    def __repr__(self):
        return f' ID: {self.id} Name: {self.name}. Surname: {self.surname}. Grade: {self.grade}. Grade next year: {self.add_to_grade}'

with app.app_context():
    db.create_all()
    if not Mokinys.query.first():
        students = [
            Mokinys(name='Juozas', surname='Juozaitis', grade=12),
            Mokinys(name='Paulius', surname='Paulaitis', grade=10),
            Mokinys(name='Maryte', surname='Margo', grade=11),
            Mokinys(name='Kazys', surname='Kelmas', grade=12),
            Mokinys(name='Julija', surname='Laukinute', grade=10)
        ]
        db.session.add_all(students)
        db.session.commit()

@app.route('/add-student', methods=['GET', 'POST'])
def new_student():
    if request.method == "GET":
        return render_template('new_student.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        grade = request.form.get('grade')
        new_student_row = Mokinys(name, surname, grade)
        db.session.add(new_student_row)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/')
def home():
    search_text = request.args.get('searchtab')
    if search_text:
        filtered_rows = Mokinys.query.filter(Mokinys.name.ilike(f'%{search_text}%')).all()
        return render_template('index.html', students_row = filtered_rows)
    all_rows = Mokinys.query.all()
    return render_template('index.html', students_row=all_rows)


app.run()
