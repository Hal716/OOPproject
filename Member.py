class Member:
    def __init__(self,name):
        self.__name = name
        self.__borrowed_books = []
#getters
    def get_name(self):
        return self.__name

    def get_borrowed_books(self):
        return self.__borrowed_books
#marking and appending the borrowed books in book
    def borrow_book(self, book):
        self.__borrowed_books.append(book)
#return book by ID
    def return_book(self, book_id):
        for book in self.__borrowed_books:
            if book.get_id() == book_id:
                self.__borrowed_books.remove(book)
                return True
        return False
    # normal member (3 books)
    def can_borrow(self):
        return len(self.__borrowed_books) < 3


#str
    def __str__(self):
        return f"Member: {self.__name} | Borrowed books: {len(self.__borrowed_books)}"
