
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///companies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String)
    no_of_employees = db.Column(db.Integer)

    employees = db.relationship('Employee', backref=backref('company'))

    def __repr__(self):
        return f'ID: {self.id}  Company name: {self.name}, Company located in: {self.city}'
    def __init__(self, name, city, no_of_employees=0):
        self.name = name
        self.city = city
        # self.no_of_employees = no_of_employees

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    position = db.Column(db.String)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __init__(self, name, surname,position, company_id):
        self.name = name
        self.surname = surname
        self.position = position
        self.company_id = company_id

    def __repr__(self):
        return f'Name {self.name}, Surname: {self.surname}, Position: {self.position} Works at {self.company.name}'


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    search_text = request.args.get("searchtab")
    search_city = request.args.get('citytab')
    if search_text or search_city:
        query = Company.query
        if search_text:
            query = query.filter(Company.name.ilike(f"%{search_text}%"))
        if search_city:
            query = query.filter(Company.city.ilike(f"%{search_city}%"))
        filtered_rows = query.all()
        return render_template("index.html", company_rows=filtered_rows)
    else:
        company_rows = Company.query.all()
        return render_template("index.html", company_rows=company_rows)

@app.route('/companies/<int:company_id>')
def one_company(company_id):
    one_company_row = Company.query.get(company_id)
    if one_company_row:
        employees = one_company_row.employees
        return render_template('one_company.html', one_company_row=one_company_row, employees=employees)
    return "bad URL :("

@app.route('/add-company', methods=['GET', 'POST'])
def add_company():
    if request.method == 'GET':
        return render_template('add_company.html')
    elif request.method == 'POST':
        name = request.form.get('namebar')
        city = request.form.get('citybar')
        new_company_row = Company(name, city)
        db.session.add(new_company_row)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit-company/<int:company_id>', methods=['GET', 'POST'])
def edit_company(company_id):
    one_company_row = Company.query.get(company_id)
    if not one_company_row:
        return 'Company doesnt exists'
    if request.method == 'GET':
        return render_template('company_edit_form.html', one_company_row=one_company_row)
    if request.method == 'POST':
        name = request.form.get('namebar')
        city = request.form.get('citybar')
        one_company_row.name = name
        one_company_row.city = city
        db.session.commit()
        return redirect(url_for('home'))

@app.route('/delete-company/<int:company_id>', methods=['POST'])
def delete_company(company_id):
    one_company_row = Company.query.get(company_id)
    if one_company_row:
        db.session.delete(one_company_row)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/employees')
def employees():
    all_employees = Employee.query.all()
    return render_template('employees.html', all_employees=all_employees )


@app.route('/add-employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'GET':
        return render_template('add_employee.html')
    elif request.method == 'POST':
        name = request.form.get('namebar')
        surname = request.form.get('surnamebar')
        position = request.form.get('positionbar')
        company_id = request.form.get('companyidbar')
        new_employee_row = Employee(name, surname, position, company_id)
        db.session.add(new_employee_row)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit-employee/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    one_employee_row = Employee.query.get(employee_id)
    if not one_employee_row:
        return 'Employee does not exist'
    if request.method == 'GET':
        return render_template('employee_edit_form.html', one_employee_row=one_employee_row)
    if request.method == 'POST':
        one_employee_row.name = request.form.get('namebar')
        one_employee_row.surname = request.form.get('surnamebar')
        one_employee_row.position = request.form.get('positionbar')
        one_employee_row.company_id = request.form.get('companyidbar')
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete-employee/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    one_employee_row = Employee.query.get(employee_id)
    if one_employee_row:
        db.session.delete(one_employee_row)
        db.session.commit()
    return redirect(url_for('home'))

app.run()