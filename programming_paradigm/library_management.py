class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def change_status(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False

    def check_status(self):
        if self.__is_checked_out == True:
            return True
        else:
            return False
    


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, Book):
        self._books.append(Book)

    def check_out_book(self, title):
        for item in self._books:
            if item.title == title:
                item.change_status()

    def return_book(self, title):
        for item in self._books:
            if item.title == title:
                item.return_book()

    def list_available_books(self):
        for item in self._books:
            if item.check_status() == False :
                print(f"{item.title} by {item.author}")
            
