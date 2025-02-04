from datetime import datetime
class Book:
    publisher = 'Penguin'
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_age(self):
        return datetime.today().year - self.year

books = [
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
]

print(books[0])
book_age_1 = books[0].get_book_age()
print(f'Book is: {book_age_1} years old')
print(f'Book is: {books[1].get_book_age()} years old')


print('-------------------')

for book in books:
    print(f'Book "{book.title}" is {book.get_book_age()} years old')