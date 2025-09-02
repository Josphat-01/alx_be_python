# library_system.py

class Book:
    """Base class representing a general book."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # call base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}MB"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)  # call base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that manages books."""

    def __init__(self):
        self.books = []  # composition: Library HAS-A list of books

    def add_book(self, book: Book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(f"{book}")
