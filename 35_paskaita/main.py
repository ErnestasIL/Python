from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/people')
def get_people():
    people = [
        {'id': 1, 'name': 'Jonas', 'age': 25 },
        {'id': 2, 'name': 'Laura', 'age': 30 },
        {'id': 3, 'name': 'Petras', 'age': 40 }
    ]
    return jsonify(people)

app.run(port=5000)