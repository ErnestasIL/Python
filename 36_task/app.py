
from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db
from models import Book

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/books', methods=['GET'])
def get_book():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])


@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], year=data['year'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404

    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.year = data.get('year', book.year)

    db.session.commit()

    return jsonify(book.to_dict())


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()

    return '', 204

app.run()
