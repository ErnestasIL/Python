from flask import Flask, render_template
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

    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = surname
        self.grade = grade

    def __repr__(self):
        return f'{self.id} {self.name} {self.surname} {self.grade} {self.creation_date}'

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


@app.route('/')
def home():
    all_rows = Mokinys.query.all()
    return render_template('index.html', students_row=all_rows)


app.run()
