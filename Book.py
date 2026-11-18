class Book:
    def __init__(self,id,title,author,copies):
        self.__id=id
        self.__title=title
        self.__author=author
        self.__copies=copies

    # getters
    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_copies(self):
        return self.__copies

    # setters
    def set_title(self,new_title):
        self.__title = new_title
    def set_author(self,new_author):
        self.__author = new_author
    def set_copies(self,new_copies):
        while True:
            if new_copies < 0:
                print("Number of copies cannot be negative.")
                return
            else:
                self.__copies = new_copies
                break

    def __str__(self):
        return f"ID: {self.__id} , title: {self.__title} , author: {self.__author} , Copies: {self.__copies}"
