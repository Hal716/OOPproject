# i've divided the code to sepreated files since it will be easier to read
from AddRmv import AddRmvBookPage
from UserLogin import UserLoginPage
from PremiumLogin import PremiumLoginPage
from BorrowReturn import BorrowReturnBookPage
from Shared import * # this file is for the images that is shared between the files

from Library import Library
# GUI library
import customtkinter as c


c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")

######### Main Application Class

class LibraryApp(c.CTk, Library):
    apperence = False # 
    def __init__(self):
        super().__init__()

        # App initialization
        self.library = Library()
        self.title("UPM Library")
        self.geometry("1000x600")
        self.minsize(1000, 600)
        self.iconbitmap("img/bs.ico")
        self.protocol("WM_DELETE_WINDOW", self.quit) # this will allow us to save even if the user close the app from the (X) button
        
        # imges
        self.bg = c.CTkImage(light_image=libimg, dark_image=libimg, size=(500, 600))   
        self.si = c.CTkImage(light_image=lightsignimg, dark_image=drksignimg, size=(70, 60))
        self.bk = c.CTkImage(light_image=bookimg, dark_image=bookimg, size=(100, 130))
        self.libfull = c.CTkImage(light_image=libfullimg, dark_image=libfullimg, size=(1000, 600))

        # Window
        
        self.main_page = MainPage(self)
        self.user_login_page = UserLoginPage(self)
        self.Premium_login_page = PremiumLoginPage(self)
        self.addrmv_book_page = AddRmvBookPage(self)
        self.borrow_return_book_page = BorrowReturnBookPage(self)

        self.show_page(self.main_page)


    def quit(self):
        self.library.save_data()
        print("Closing the app...")
        self.destroy()

    def show_page(self, page):
        # Hide all pages
        for widget in self.winfo_children():
            widget.pack_forget()

        # Show the selected page
        page.pack(fill="both", expand=True)

    def tuggel_theme(self, theme):
        if not LibraryApp.apperence:
            c.set_appearance_mode("light")
            theme.configure(image=dark_image)
            self.si.configure(image=dark_image)
            LibraryApp.apperence = True
        else:
            c.set_appearance_mode("dark")
            theme.configure(image=light_image)
            self.si.configure(image=light_image)
            
            LibraryApp.apperence = False

######### Main Frame Page
 
class MainPage(c.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #window design
        self.bglablel = c.CTkLabel(self, image=master.bg, text="")
        self.bglablel.place(x=0, y=0, anchor="nw")

        self.silabel = c.CTkLabel(self, image=master.si, text="")
        self.silabel.place(x=500, y=20)

        self.bklabel = c.CTkLabel(self, image=master.bk, text="", fg_color="transparent")
        self.bklabel.place(x=510, y=470)

        self.main_farme = c.CTkFrame(self, width=500, height=600, fg_color="transparent")
        self.main_farme.pack( anchor="e", fill="both", side="right", ipadx=50)

        # change Window Theme (and it's the same button for all frames)
        theme = self.theme_button = c.CTkButton(self.main_farme, image=light_image, text="", width=30, height=30, fg_color="transparent", command=lambda: master.tuggel_theme(theme), hover_color="#929292")
        theme.place(relx=0.988, rely=0.03, anchor="ne")

        self.label = c.CTkLabel(self.main_farme, text="Welcom to UPM Library", font=("Times", 24, 'bold'), bg_color="transparent", text_color="#A77338")
        self.label.grid(row=1, column=1, pady=50, padx=20)


        # Buttons
        self.user_btn = c.CTkButton(self.main_farme, text="User Login", command=lambda: master.show_page(master.user_login_page), fg_color="#6A4A26", hover_color="#8B5E3C")
        self.user_btn.grid(row=2, column=1, pady=20, padx=20)

        self.premium_btn = c.CTkButton(self.main_farme, text="Premium Login", command=lambda: master.show_page(master.Premium_login_page), fg_color="#6A4A26", hover_color="#8B5E3C")
        self.premium_btn.grid(row=3, column=1, pady=20, padx=20)
        
        self.addrmv_btn = c.CTkButton(self.main_farme, text="(Add / Remove) Book", command=lambda: master.show_page(master.addrmv_book_page), fg_color="#6A4A26", hover_color="#8B5E3C")
        self.addrmv_btn.grid(row=4, column=1, pady=20, padx=20)

        self.returnborrow_btn = c.CTkButton(self.main_farme, text="(Return / Borrow) Book", command=lambda: master.show_page(master.borrow_return_book_page), fg_color="#6A4A26", hover_color="#8B5E3C")
        self.returnborrow_btn.grid(row=5, column=1, pady=20, padx=20)

        self.exit = c.CTkButton(self.main_farme, text="Exit", command=lambda: master.quit(), fg_color="#6A4A26", hover_color="#8B5E3C")
        self.exit.grid(row= 20, column=1, pady=20)

        # Note! (lambda) is used to simple the way (it's just to not define a new fuction to use the master methods like show_page())






lib = LibraryApp()
lib.mainloop()