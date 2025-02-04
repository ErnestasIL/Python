class Car:
    manufacturer = 'Toyota'

class Bike:
    manufacturer = 'Yamaha'

print(Car.manufacturer)
print(Bike.manufacturer)


class Book:
    publisher = 'Penguin'
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book('Harry Potter', 'J.K Rowling', 1997)
book2 = Book('House of dragon', 'JJ Martin', 2005)

print(book1.title, book1.year)
print(book2.title, book2.year)