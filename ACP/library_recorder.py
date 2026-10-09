class Book:
    def __init__(self, title):
        self.title = title
        self.borrowed = False
    def borrow(self):
        self.borrowed = True
        print("Book borrowed!")
    def return_book(self):
        self.borrowed = False
        print("Book returned!")
    def __str__(self):
        return self.title
b1 = Book("Harry Potter")
print(b1)
b1.borrow()
b1.return_book()