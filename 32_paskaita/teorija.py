from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai_2_lent.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Projektas(db.Model):
    __tablename__ = "projektas"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String)
    kaina = db.Column(db.Float)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)
    atlikti_darbai = db.relationship("AtliktasDarbas", backref="projektas", cascade="all, delete-orphan")

    def __init__(self, pavadinimas, kaina):
        self.pavadinimas = pavadinimas
        self.kaina = kaina

    @property
    def kaina_su_pvm(self):
        return round(self.kaina * 1.21)

class AtliktasDarbas(db.Model):
    __tablename__ = "atliktas_darbas"
    id = db.Column(db.Integer, primary_key=True)
    darbas = db.Column(db.String)
    samata = db.Column(db.Float)
    imone = db.Column(db.String)
    projektas_id = db.Column(db.Integer, db.ForeignKey("projektas.id"), nullable=False)

    def __init__(self):

with app.app_context():
    db.create_all()

# @app.route('/')
# def home():
#     search_text = request.args.get('searchlaukelis')
#     if search_text:
#         filtered_rows = Projektas.query.filter(Projektas)

if __name__ == '__main__':
    app.run()
