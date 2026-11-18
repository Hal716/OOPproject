import customtkinter as c
from Member import Member
from Shared import *

######### User Login Page

class UserLoginPage(c.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.mas = self.master
        self.main = self.mas.library


        #window design
        self.bglablel = c.CTkLabel(self, image=master.libfull, text="")
        self.bglablel.place(x=0, y=0)


        self.user_frame = c.CTkFrame(self, width=1000, height=550, fg_color="transparent")
        self.user_frame.place(relx=0.5, rely=0.15, anchor="n", relwidth=1, relheight=1)

        theme = self.theme_button = c.CTkButton(self.user_frame, image=light_image, text="", width=30, height=30, fg_color="transparent", command=lambda: master.tuggel_theme(theme), hover_color="#929292")
        theme.place(relx=0.988, rely=0.05, anchor="ne")

        # Back to Main menu button
        self.btn_back = c.CTkButton(self.user_frame, text="",command=lambda: master.show_page(master.main_page), fg_color="transparent", hover_color="#929292", image=White_home , width=30, height=30)
        self.btn_back.pack(pady=30, side="left", anchor="nw", padx=10)

        label = c.CTkLabel(self.user_frame, text="User Login Page", font=("Times", 24, 'bold'), fg_color="transparent", text_color="#A77338")
        label.pack(pady=35)

        space= c.CTkLabel(self.user_frame, text="", fg_color="transparent")
        space.pack(pady=20) # just a space between label and entry to make it look better


        self.username_entry = c.CTkEntry(self.user_frame, placeholder_text="Username")
        self.username_entry.pack(pady=10)

        # this label jop is to show login status (success or fail)
        self.login_text = c.CTkLabel(self.user_frame, text="", fg_color="transparent")
        self.login_text.pack(pady=1)

        # we
        self.login_button = c.CTkButton(self.user_frame, text="Login", command=self.login, fg_color="#6A4A26", hover_color="#8B5E3C")
        self.login_button.pack(pady=10)

        space2= c.CTkLabel(self.user_frame, text="", fg_color="transparent")
        space2.pack(pady=20) # another space (i love evrything to be clean) :)
        
        self.available_members = c.CTkScrollableFrame(self.user_frame, width=300, height=275, label_text="Availble Members", )
        self.available_members.place(x=0, y=120 ,anchor="nw")

        

        self.refrech_members_list()
    def login(self):
        username = self.username_entry.get()
        
        if username == "":
            self.login_text.configure(text="Please enter a username.", text_color="red")
            return
        else:
            app = self.master   
            library = app.library
            library.set_members(username)
            self.login_text.configure(text="Login Successful!", text_color="green")
            self.add_members_list()

    def add_members_list(self):
        new_user= c.CTkButton(self.available_members, text=f"{self.username_entry.get()}", fg_color="transparent", anchor="w", hover_color="#8B5E3C", font=("Comic Sans MS", 12, "bold"))
        new_user.pack(pady=5)

    def refrech_members_list(self):
        for member in self.main.members:
            new_user= c.CTkButton(self.available_members, text=f"{member}", fg_color="transparent", anchor="w", hover_color="#8B5E3C", font=("Comic Sans MS", 12, "bold"))
            new_user.pack(pady=5)


