from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import date, timedelta

engine = create_engine('sqlite:///library.db')
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    author = Column(String, nullable=False)
    year_published = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)
    borrowed_books = relationship('BorrowedBook', back_populates='book')

class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    borrowed_books = relationship('BorrowedBook', back_populates='reader')

class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    reader_id = Column(Integer, ForeignKey('readers.id'), nullable=False)
    borrowed_at = Column(Date, nullable=False)
    return_due_date = Column(Date, nullable=False)
    book = relationship('Book', back_populates='borrowed_books')
    reader = relationship('Reader', back_populates='borrowed_books')


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_book():
    title = input('Enter book title: ')
    author = input('Enter book author: ')
    year = int(input('Enter year published: '))
    book = Book(title=title, author=author, year_published=year)
    session.add(book)
    session.commit()
    print('Book added')


def add_reader():
    name = input('Enter reader name: ')
    email = input('Enter reader email: ')
    if session.query(Reader).filter_by(email=email).first():
        print('Error: Email already exists')
        return

    reader = Reader(name=name, email=email)
    session.add(reader)
    session.commit()
    print('Reader added')

def lend_book():
    try:
        book_id = int(input('Enter book ID: '))
    except ValueError:
        print('Invalid input! Please enter a valid number.')
        return
    reader_id = int(input('Enter reader ID: '))
    book = session.query(Book).filter_by(id=book_id, available=True).first()
    if not book:
        print('Book is not available')
        return
    borrowed_at = date.today()
    return_due_date = borrowed_at + timedelta(days=14)
    borrowed_book = BorrowedBook(book_id=book_id, reader_id=reader_id, borrowed_at=borrowed_at, return_due_date=return_due_date)
    book.available = False
    session.add(borrowed_book)
    session.commit()
    print('Book lent ')

def update_book():
    try:
        book_id = int(input('Enter book ID: '))
    except ValueError:
        print('Invalid input! Please enter a valid number.')
        return
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print("Book not found!")
        return
    book.title = input(f'Enter new title ({book.title}): ') or book.title
    book.author = input(f'Enter new author ({book.author}): ') or book.author
    session.commit()
    print('Book updated')

def delete_book():
    try:
        book_id = int(input('Enter book ID: '))
    except ValueError:
        print('Invalid input! Please enter a valid number.')
        return
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print('Book not found!')
        return
    session.delete(book)
    session.commit()
    print('Book deleted')

def delete_reader():
    reader_id = int(input('Enter reader ID to delete: '))
    reader = session.query(Reader).filter_by(id=reader_id).first()
    if not reader:
        print('Reader not found!')
        return
    session.delete(reader)
    session.commit()
    print('Reader deleted')


def list_books():
    books = session.query(Book).all()
    for book in books:
        status = 'Available' if book.available else 'Borrowed'
        print(f'{book.id}: {book.title} by {book.author} ({book.year_published}) - {status}')
    print()

def list_borrowed_books():
    borrowed_books = session.query(BorrowedBook).all()
    for bb in borrowed_books:
        book = session.query(Book).filter_by(id=bb.book_id).first()
        reader = session.query(Reader).filter_by(id=bb.reader_id).first()
        print(f'{book.title} borrowed by {reader.name} (Due: {bb.return_due_date})')
    print()


def view_reader_history():
    try:
        reader_id = int(input('Enter reader ID: '))
    except ValueError:
        print('Invalid input! Please enter a valid number.')
        return
    reader = session.query(Reader).filter_by(id=reader_id).first()
    if not reader:
        print('Reader not found!')
        return
    borrowed_books = session.query(BorrowedBook).filter_by(reader_id=reader_id).all()
    if not borrowed_books:
        print(f'No borrowing history for {reader.name}.')
        return
    print(f'Borrowing history for {reader.name}:')
    for bb in borrowed_books:
        book = session.query(Book).filter_by(id=bb.book_id).first()
        print(f'{book.title} (Borrowed at: {bb.borrowed_at}, Due: {bb.return_due_date})')
    print()

while True:
    print('Library')
    print('1. Add book')
    print('2. Add reader')
    print('3. Lend book')
    print('4. Update book')
    print('5. Delete book')
    print('6. Delete reader')
    print('7. List books')
    print('8. List borrowed books')
    print('9. View reader history: ')
    print('10. Exit')
    choice = input('Choose an option: ')
    if choice == '1':
        add_book()
    elif choice == '2':
        add_reader()
    elif choice == '3':
        lend_book()
    elif choice == '4':
        update_book()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        delete_reader()
    elif choice == '7':
        list_books()
    elif choice == '8':
        list_borrowed_books()
    elif choice == '9':
        view_reader_history()
    elif choice == '10':
        print('Goodbye :)')
        break
    else:
        print("Invalid option. Try again.")
