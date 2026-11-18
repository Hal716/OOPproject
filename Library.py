from Book import Book
from Member import Member
from PremiumMember import PremiumMember
import json

#using random IDs because the ID gen is kinda tricky for this project
import random

class Library:

    # maximum number of books allowed in the library
    MAX_BOOKS = 10

    def __init__(self):
        # list that stores all available books
        self.available_books = [
            Book(1,"Clean Code", "Robert C. Martin", 3),
            Book(2,"Python Crash Course", "Eric Matthes", 4),
            Book(3,"The Pragmatic Programmer", "Andrew Hunt", 2),
            Book(4,"The Hobbit", "J.R.R. Tolkien", 5),
            Book(5,"Introduction to Algorithms", "Cormen et al.", 1),
        ]


        self.borrowed_books = []
        self.history = []
        self.members = []

        self.load_data()

    # print all added members
    def print_member(self):
        for member in self.members:
            print(member)

    def set_members(self, member):
        new_member = Member(member)
        
        self.members.append(new_member)

    def set_premium_members(self, member):
        new_member = PremiumMember(member)
        
        self.members.append(new_member)

    def check_member(self, name):
        for member in self.members:
            if member.get_name() == name:
                return True
        return False
    
    def get_member(self, member):
        for names in self.members:
            if names.get_name() == member:
                member = names
                break
        return member

    def is_full(self):
        if len(self.available_books) > self.MAX_BOOKS:
            return True
        else:
            return False



    # generate a random book ID that is not already used
    def generate_unique_book_id(self):

        # if library is full, do not add more books
        if len(self.available_books) >= self.MAX_BOOKS:
            print("Library is full. Cannot add more books.")

        # store all used IDs
        used_ids = []
        for book in self.available_books:
            used_ids.append(book.get_id())

        # while loop for new IDs
        while True:
            new_id = random.randint(1, self.MAX_BOOKS)
            if new_id not in used_ids:
                return new_id


    # add a new book to the library
    def add_new_books(self):

        # if library is not full
        if len(self.available_books) < self.MAX_BOOKS:

            # take book info from user
            new_book_title = input("Enter new book title: ")
            new_book_author = input("Enter new book author: ")

            # while loop to check if copies are positive
            while True:
                new_book_copies = int(input("Enter new book copies: "))
                if new_book_copies <= 0:
                    print("Number of copies cannot be negative or zero.")
                else:
                    break

            # generate unused ID for the book
            new_id = self.generate_unique_book_id()

            # create new book object
            book = Book(new_id, new_book_title, new_book_author, new_book_copies)

            # add book to the list
            self.available_books.append(book)

            print(f"New book added with ID: {new_id} and title: {new_book_title}")

        else:
            print("Library is full. Cannot add more books.")
            return False


    # remove a book from the library by using the IDs
    def remove_book(self):

        id_to_remove_book = int(input("Enter book id that you want to remove: "))

        # search for the book
        for book in self.available_books:
            if book.get_id() == id_to_remove_book:
                self.available_books.remove(book)
                print(f"The Book {book.get_title()} has been removed.")
                break
        else:
            print(f"No book with ID {id_to_remove_book} found.")


    # register new member
    def register_new_members(self):

        new_member_name = input("Enter new member name: ")

        # create new member object
        member = Member(new_member_name)

        # add member to the list
        self.members.append(member)

        print(f"{new_member_name} has been added as a new member.")


#########################################################################################################
# PHASE 2


    # borrow a book
    def borrow_books(self):

        # take member name and book title
        member_name = input("Enter member name : ")
        book_title = input("Enter book title : ")

        the_member = None
        the_book = None

        # find the member by name
        for m in self.members:
            if m.get_name().lower() == member_name.lower():
                the_member = m
                break

        # check if member is there
        if the_member is None:
            print("Member not found.")
            return

        # find the book by title
        for b in self.available_books:
            if b.get_title().lower() == book_title.lower():
                the_book = b
                break

        # check if book is there
        if the_book is None:
            print("Book not found.")
            return

        # check if copies available
        if the_book.get_copies() <= 0:
            print("No copies available.")
            return

        # reduce copies by 1 after borrowing
        the_book.set_copies(the_book.get_copies() - 1)

        # add book to member borrowed list
        the_member.borrow_book(the_book)

        # add book to borrowed list
        self.borrowed_books.append(the_book)

        print(f"{the_member.get_name()} borrowed {the_book.get_title()} successfully.")
        self.history.append(f"{the_member.get_name()} borrowed {the_book.get_title()}")



    # return a borrowed book
    def return_books(self):

        # take member name and book ID
        member_name = input("Enter member name : ")
        book_id = int(input("Enter book ID to return : "))

        the_member = None

        # find the member
        for m in self.members:
            if m.get_name().lower() == member_name.lower():
                the_member = m
                break

        # if member is not there x2
        if the_member is None:
            print("Member not found.")
            return

        # return the book from member if there
        returned = the_member.return_book(book_id)

        if returned:
            # increase the copies after returning
            for b in self.available_books:
                if b.get_id() == book_id:
                    b.set_copies(b.get_copies() + 1)
                    print("Book returned successfully.")
                    self.history.append(f"{the_member.get_name()} returned {b.get_title()}")
                    return
        else:
            print("This member did not borrow this book.")


    # display all books borrowed by member name
    def display_member_borrowed_books(self):

        member_name = input("Enter member name : ")

        # search for the member
        for m in self.members:
            if m.get_name().lower() == member_name.lower():

                print("\nBorrowed books: ")

                if len(m.get_borrowed_books()) == 0:
                    print("No borrowed books.")
                else:
                    for b in m.get_borrowed_books():
                        print(b)
                return

        print("Member not found.")


    # display all books sorted by title
    def display_all_books_sorted(self):

        # make another copy so original list stays the same
        sorted_books = self.available_books.copy()

        # simple sorting using two for loops
        for i in range(len(sorted_books)):
            for j in range(i + 1, len(sorted_books)):

                # if first title is greater than second, swap them
                if sorted_books[i].get_title() > sorted_books[j].get_title():
                    temp = sorted_books[i]
                    sorted_books[i] = sorted_books[j]
                    sorted_books[j] = temp

        # print books after sorting
        print("All Books (Sorted by Title):")
        for book in sorted_books:
            print(book)


####################################################################################################
# PHASE 3

    def save_data(self):
        data = {
            "books": [{
                "id": b.get_id(),
                "title": b.get_title(),
                "author": b.get_author(),
                "copies": b.get_copies()
            } for b in self.available_books],

            "members": [{
                "name": m.get_name(),
                "type": "premium" if isinstance(m, PremiumMember) else "normal",
                "borrowed": [book.get_id() for book in m.get_borrowed_books()]
            } for m in self.members],

            "history": self.history
        }

        with open("library_data.txt", "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open("library_data.txt", "r") as file:
                data = json.load(file)

            # Load books
            self.available_books = []
            for b in data["books"]:
                book = Book(b["id"], b["title"], b["author"], b["copies"])
                self.available_books.append(book)

            # Load members
            self.members = []
            for m in data["members"]:
                if m["type"] == "premium":
                    member = PremiumMember(m["name"])
                else:
                    member = Member(m["name"])
                self.members.append(member)

            # attach borrowed books
            for m, saved in zip(self.members, data["members"]):
                for book_id in saved["borrowed"]:
                    for book in self.available_books:
                        if book.get_id() == book_id:
                            m.borrow_book(book)

            # history
            self.history = data["history"]

        except:
            print("No saved data found.")

    def show_history(self):
        print("\nTransaction History:")
        if len(self.history) == 0:
            print("No history yet.")
        else:
            for h in self.history:
                print(h)
