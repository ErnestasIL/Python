import datetime


class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self.borrow_date = None

    def __str__(self):
        return f'{self.title} by {self.author} ({self.year}) - {"Available" if self.available else "Not Available"}'

    def is_classic(self):
        return datetime.datetime.now().year - self.year > 50

    def borrow(self):
        if self.available:
            self.available = False
            self.borrow_date = datetime.datetime.now()
            return True
        return False

    def return_book(self):
        self.available = True
        self.borrow_date = None

    def due_date(self):
        if self.borrow_date:
            return self.borrow_date + datetime.timedelta(days=21)
        return None


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        try:
            for book in self.books:
                if book.title.lower() == title.lower() and book.available:
                    book.borrow()
                    print(f"You have borrowed: '{book.title}'. Due date: {book.due_date().strftime('%Y-%m-%d')}")
                    return
            raise ValueError('Book is not available or does not exist.')
        except ValueError:
            print(ValueError)

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.return_book()
                print(f'You have successfully returned: "{book.title}"')
                return
        print('Book was not found or you did not borrow it.')

    def filter_books(self, *args, **kwargs):
        filtered_books = self.books
        for key, value in kwargs.items():
             if key == 'title':
                 filtered_books = [book for book in filtered_books if book.title.lower() == value.lower()]
             elif key == 'author':
                 filtered_books = [book for book in filtered_books if book.author.lower() == value.lower()]
             elif key =='year':
                 filtered_books = [book for book in filtered_books if book.year == value]
        if filtered_books:
             for book in filtered_books:
                 print(book)
        else:
             print('No match found')


library = Library()

while True:
    print('\nLibrary management system:\n')
    print('1. Add a book to the library')
    print('2. Display available books')
    print('3. Borrow a book')
    print('4. Return a book')
    print('5. Filter available books')
    print('6. Exit and close the program')
    choice = input('Enter your choice: ')
    if choice == '1':
        title = input('Enter book title: ')
        author = input('Enter book author: ')
        try:
            year = int(input('Enter book year: '))
            library.add_book(Book(title, author, year))
            print('Book has been added successfully.')
        except ValueError:
            print('Invalid year format')
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        title = input('Enter book title you want to borrow: ')
        library.borrow_book(title)
    elif choice == '4':
        title = input('Enter book title you want to return: ')
        library.return_book(title)
    elif choice == '5':
        print('\nFilter options:')
        print('1. Filter by title')
        print('2. Filter by author')
        print('3. Filter by year')
        filter_choice = input('Enter your filter choice: ')
        if filter_choice == '1':
            title = input('Enter book title: ')
            library.filter_books(title=title)
        elif filter_choice == '2':
             author = input('Enter authors name: ')
             library.filter_books(author=author)
        elif filter_choice == '3':
            year = int(input('Enter book year: '))
            library.filter_books(year=year)
        else:
            print('Invalid filter choice.')
    elif choice == '6':
        print('Program closing down... Goodbye!')
        break
    else:
        print('Invalid choice, try again')