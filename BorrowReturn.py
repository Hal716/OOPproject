import customtkinter as c
from Library import Library
from Book import Book
from Member import Member
from Shared import *

######### Borrow / Return Book Page

class BorrowReturnBookPage(c.CTkFrame):
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

        label = c.CTkLabel(self.frame, text="Brrow / Return Book Page", font=("Times", 24, 'bold'), fg_color="transparent", text_color="#A77338")
        label.pack(pady=35)
        

        self.add_frame = c.CTkFrame(self.frame, width=330, height=400, border_width=2 ,border_color="#A77338")
        self.add_frame.pack(side="left", expand=True, fill="both", padx=20, pady=20)

        # get User ID so he can borrow/return books by his name

        user_check_frame = c.CTkFrame(self.add_frame, width=600, height=400, border_width=2 ,border_color="#FFFFFF")
        user_check_frame.pack(pady=50, expand=True, padx=20)

        user_label = c.CTkLabel(user_check_frame, text="Enter User ID to proceed", font=("Comic Sans MS", 16), fg_color="transparent", text_color="#FFFFFF")
        user_label.pack(pady=20, padx=80)

        self.user_id_entry = c.CTkEntry(user_check_frame, placeholder_text="User ID")
        self.user_id_entry.pack(pady=10, padx=80)


        self.user_id_btn = c.CTkButton(user_check_frame, text="Login", fg_color="#6A4A26", hover_color="#8B5E3C", command=self.proceed_user)
        self.user_id_btn.pack(pady=20, padx=80)

        self.user_check_text = c.CTkLabel(user_check_frame, text="", fg_color="transparent")
        self.user_check_text.pack(pady=10, padx=80)

        # Main Brrrow / Return Frame will be here after user ID is verified

        self.RB_frame = c.CTkFrame(self.add_frame, width=650, height=450, border_width=2)

        self.RB_label = c.CTkLabel(self.RB_frame, text="", font=("Comic Sans MS", 20), fg_color="transparent", text_color="#FFFFFF")
        self.RB_label.pack(pady=20)

        self.borrow_frame = c.CTkFrame(self.RB_frame, width=300, height=400, border_width=2 ,border_color="#A77338")
        self.borrow_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

        available_books_frame = c.CTkFrame(self.RB_frame, width=150, height=400, border_width=2 ,border_color="#A77338")
        available_books_frame.pack(side="left", expand=True ,fill="both", padx=20, pady=10)

        self.return_frame = c.CTkFrame(self.RB_frame, width=300, height=400, border_width=2 ,border_color="#A77338")
        self.return_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        # Brrow section
        borrow_label = c.CTkLabel(self.borrow_frame, text="Borrow Book", font=("Comic Sans MS", 20), fg_color="transparent", text_color="#FFFFFF")
        borrow_label.pack(pady=10)

        self.borrow_id_entry = c.CTkEntry(self.borrow_frame, placeholder_text="Book ID")
        self.borrow_id_entry.pack(pady=10)

        self.borrow_text = c.CTkLabel(self.borrow_frame, text="", fg_color="transparent")
        self.borrow_text.pack(pady=5)

        self.borrow_btn = c.CTkButton(self.borrow_frame, text="Borrow Book", fg_color="#6A4A26", hover_color="#8B5E3C", command=self.borrow_book)
        self.borrow_btn.pack(pady=20)

        # Return section
        return_label = c.CTkLabel(self.return_frame, text="Return Book", font=("Comic Sans MS", 20), fg_color="transparent", text_color="#FFFFFF")
        return_label.pack(pady=10)

        self.return_id_entry = c.CTkEntry(self.return_frame, placeholder_text="Book ID")
        self.return_id_entry.pack(pady=10)

        self.return_text = c.CTkLabel(self.return_frame, text="", fg_color="transparent")
        self.return_text.pack(pady=5)

        self.return_btn = c.CTkButton(self.return_frame, text="Return Book", fg_color="#6A4A26", hover_color="#8B5E3C", command=self.return_book)
        self.return_btn.pack(pady=20)
        
        # Available Books Section
        availb_label = c.CTkLabel(available_books_frame, text="Available Books", font=("Comic Sans MS", 20), fg_color="transparent", text_color="#FFFFFF")
        availb_label.pack(pady=20)

        self.avail_books_textbox = c.CTkTextbox(available_books_frame, width=150, height=200)
        self.avail_books_textbox.pack(pady=10, expand=True, fill="both", padx=10)
        self.refresh_books_list()       

         
        # Back to Main menu button
        self.btn_back = c.CTkButton(self, text="", image=White_home , width=30, height=30, command=lambda: master.show_page(master.main_page), fg_color="transparent", hover_color="#929292")
        self.btn_back.pack(pady=100, side="left", anchor="nw", padx=10)

    # Main Methods

    def proceed_user(self):
        self.username = self.user_id_entry.get()
        if self.library.check_member(self.username):
            for widget in self.add_frame.winfo_children():
                widget.pack_forget()
            
            self.RB_frame.pack(side="left", expand=True, fill="both", padx=20, pady=20)
            self.RB_label.configure(text = f"Welcome {self.username}")

    
        else:
            self.user_check_text.configure(text="User ID not found. Please try again.", text_color="#FF0000")
        return
    
    def borrow_book(self):
        borrow_id = int(self.borrow_id_entry.get())
        the_book = None
        self.member = self.library.get_member(self.username)


        for book in self.library.available_books:
            if book.get_id() == borrow_id:
                the_book = book
                break
        if the_book is None:
            self.borrow_text.configure(text="Book ID not found. Please try again.", text_color="#FF0000")
            return
        
        if book.get_copies() <= 0:
            self.borrow_text.configure(text="No copies available for this book.", text_color="#FF0000")
            return
        
        the_book.set_copies(the_book.get_copies() - 1)        
        self.member.borrow_book(the_book)
        self.library.borrowed_books.append(the_book)
        self.borrow_text.configure(text="Book Borrowed succefully", text_color="green")
        self.refresh_books_list()
    
    def return_book(self):
        return_id = int(self.return_id_entry.get())
        the_book = None
        self.member = self.library.get_member(self.username)

        for book in self.library.available_books:
            if book.get_id() == return_id:
                the_book = book
                break

        if the_book is None:
            self.return_text.configure(text="Book ID not found. Please try again.", text_color="#FF0000")
            return
        
        returned = self.member.return_book(return_id)

        if returned:
            # increase the copies after returning
            for b in self.library.available_books:
                if b.get_id() == return_id:
                    b.set_copies(b.get_copies() + 1)
                    self.return_text.configure(text="Book returned successfully", text_color="green")
                    self.library.history.append(f"{self.member.get_name()} returned {b.get_title()}")
        else:
            self.return_text.configure(text="This member did not borrow this book.", text_color="#FF0000")
        self.refresh_books_list()



        
        
            
    def refresh_books_list(self):
        self.avail_books_textbox.delete("1.0", "end")
        self.avail_books_textbox.insert("end", "Books in Library:\n\n")
        for b in self.library.available_books:
            self.avail_books_textbox.insert("end", f"ID: {b.get_id()}, Title: {b.get_title()}, Author: {b.get_author()}, Copies: {b.get_copies()}\n")