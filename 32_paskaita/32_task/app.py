from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    orders = db.relationship('Order', backref='table', cascade='all, delete-orphan')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)

@app.route('/')
def index():
    tables = Table.query.all()
    return render_template('index.html', tables=tables)

@app.route('/add_table', methods=['POST'])
def add_table():
    number = request.form['number']
    seats = request.form['seats']
    new_table = Table(number=number, seats=seats)
    db.session.add(new_table)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/table/<int:table_id>')
def table_orders(table_id):
    table = Table.query.get_or_404(table_id)
    return render_template('table.html', table=table)

@app.route('/add_order', methods=['POST'])
def add_order():
    description = request.form['description']
    price = request.form['price']
    table_id = request.form['table_id']
    new_order = Order(description=description, price=price, table_id=table_id)
    db.session.add(new_order)
    db.session.commit()
    return redirect(url_for('table_orders', table_id=table_id))

@app.route('/delete_table/<int:table_id>', methods=['POST'])
def delete_table(table_id):
    table = Table.query.get_or_404(table_id)
    if table.orders:
        return "Cannot delete a table with existing orders!"
    db.session.delete(table)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
