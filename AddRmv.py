import customtkinter as c
from Book import Book
from Shared import *


######### Add / Remove Book Page

class AddRmvBookPage(c.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        main = self.master
        self.library = main.library

        #window design
        self.bglablel = c.CTkLabel(self, image=master.libfull, text="")
        self.bglablel.place(x=0, y=0)


        self.frame = c.CTkFrame(self, width=1000, height=550, fg_color="transparent")
        self.frame.place(relx=0.5, rely=0.15, anchor="n", relwidth=1, relheight=1)

        theme = self.theme_button = c.CTkButton(self.frame, image=light_image, text="", width=30, height=30, fg_color="transparent", command=lambda: master.tuggel_theme(theme), hover_color="#929292")
        theme.place(relx=0.988, rely=0.01, anchor="ne")

        label = c.CTkLabel(self.frame, text="Add / Remove Book Page", font=("Times", 24, 'bold'), fg_color="transparent", text_color="#A77338")
        label.pack(pady=35)
        

        add_frame = c.CTkFrame(self.frame, width=330, height=400, border_width=2 ,border_color="#A77338")
        add_frame.pack(side="left", expand=True, fill="both", padx=20, pady=20)

        available_books_frame = c.CTkFrame(self.frame, width=150, height=400, border_width=2 ,border_color="#A77338")
        available_books_frame.pack(side="left", expand=True ,fill="both", padx=20, pady=10)

        rmv_frame = c.CTkFrame(self.frame, width=330, height=400, border_width=2 ,border_color="#A77338")
        rmv_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)


        # Add Book Section
        addb_label = c.CTkLabel(add_frame, text="Add New Book", font=("Comic Sans MS", 20), fg_color="transparent", text_color="#FFFFFF")
        addb_label.pack(pady=20)

        self.add_name_entry = c.CTkEntry(add_frame, placeholder_text="Book Title")
        self.add_name_entry.pack(pady=10)

        self.add_author_entry = c.CTkEntry(add_frame, placeholder_text="Book Author")
        self.add_author_entry.pack(pady=10)

        self.add_copies_entry = c.CTkEntry(add_frame, placeholder_text="Number of Copies")
        self.add_copies_entry.pack(pady=10)

        self.add_text = c.CTkLabel(add_frame, text="", fg_color="transparent")
        self.add_text.pack(pady=5)

        self.add_btn = c.CTkButton(add_frame, text="Add Book", fg_color="#6A4A26", hover_color="#8B5E3C", command=self.add_book)
        self.add_btn.pack(pady=20)


        # rmv Book Section
        rmvb_label = c.CTkLabel(rmv_frame, text="Remove Book", font=("Comic Sans MS", 20), fg_color="transparent", text_color="#FFFFFF")
        rmvb_label.pack(pady=20)

        self.rmv_id_entry = c.CTkEntry(rmv_frame, placeholder_text="Book ID")
        self.rmv_id_entry.pack(pady=10)

        self.rmv_text = c.CTkLabel(rmv_frame, text="", fg_color="transparent")
        self.rmv_text.pack(pady=5)

        self.rmv_btn = c.CTkButton(rmv_frame, text="Remove Book", fg_color="#6A4A26", hover_color="#8B5E3C", command=self.remove_book)
        self.rmv_btn.pack(pady=20)

        # Available Books Section
        availb_label = c.CTkLabel(available_books_frame, text="Available Books", font=("Comic Sans MS", 20), fg_color="transparent", text_color="#FFFFFF")
        availb_label.pack(pady=20)

        self.avail_books_textbox = c.CTkTextbox(available_books_frame, width=150, height=200)
        self.avail_books_textbox.pack(pady=10, expand=True, fill="both", padx=10)
        self.refresh_books_list()
        
        # Back to Main menu button
        self.btn_back = c.CTkButton(self, text="", image=White_home , width=30, height=30, command=lambda: master.show_page(master.main_page), fg_color="transparent", hover_color="#929292")
        self.btn_back.pack(pady=100, side="left", anchor="nw", padx=10)

    def add_book(self):
        
        title = self.add_name_entry.get()
        author = self.add_author_entry.get()
        copies = int(self.add_copies_entry.get())

        if  self.library.is_full():
            self.add_text.configure(text="Library is full. Cannot add more books.", text_color="red")
        
        else:
            new_id = self.library.generate_unique_book_id()
            book = Book(new_id, title, author, int(copies))
            self.library.available_books.append(book)
            self.add_text.configure(text=f"New book added with ID: {new_id} and title: {title}", text_color="green")
        self.refresh_books_list()

    
    def remove_book(self):

        book_to_remove = int(self.rmv_id_entry.get())

        for book in self.library.available_books:
            if book.get_id() == book_to_remove:
                self.library.available_books.remove(book)
                self.rmv_text.configure(text=f"The Book {book.get_title()} has been removed.", text_color="green")
                break
        else:
            self.rmv_text.configure(text=f"No book with ID {book_to_remove} found.", text_color="red")

        self.refresh_books_list()

    def refresh_books_list(self):
        self.avail_books_textbox.delete("1.0", "end")
        self.avail_books_textbox.insert("end", "Books in Library:\n\n")
        for b in self.library.available_books:
            self.avail_books_textbox.insert("end", f"ID: {b.get_id()}, Title: {b.get_title()}, Author: {b.get_author()}, Copies: {b.get_copies()}\n")
        
