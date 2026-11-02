class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print('Book ID:', self.book_id)
        print('Title:', self.title)
        print('Author:', self.author)
        print('Price:', self.price)
        print()

b1 = Book(1, 'Python Programming', 'Guido van Rossum', 450)
b2 = Book(2, 'Data Structures', 'Mark Allen', 550)
b3 = Book(3, 'Clean Code', 'Robert Martin', 650)

b1.display()
b2.display()
b3.display()
