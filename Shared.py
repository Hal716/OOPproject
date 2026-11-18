import customtkinter as c
from PIL import Image

drksignimg = Image.open("img/llib.png")
lightsignimg = Image.open("img/signlib.png")
bookimg = Image.open("img/book.png")
libimg = Image.open("img/bglibn.jpg")
libfullimg = Image.open("img/bglib.jpg")
dark_image = c.CTkImage(
    dark_image=Image.open("img/moon.png"),
    size=(25, 25)
)
light_image = c.CTkImage(
    light_image=Image.open("img/sun.png"),
    size=(25, 25)
)
Dark_home = c.CTkImage(
    dark_image=Image.open("img/Dhome.png"),
    size=(25,25)
)    
White_home = c.CTkImage(
    Image.open("img/Whome.png"),
    size=(25,25)
)

