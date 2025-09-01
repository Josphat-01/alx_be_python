# library_management.py

class Book:
    def __init__(self, title, author):
        """Initialize a book with title and author. By default, it is available."""
        self.title = title
        self.author = author
        self._is_checked_out = False   # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available again if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize an empty library with a private book list."""
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            print(f'Book "{book.title}" by {book.author} added to library.')
        else:
            print("Only Book instances can be added to the library.")

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f'Book "{book.title}" has been checked out.')
                    return True
                else:
                    print(f'Sorry, "{book.title}" is already checked out.')
                    return False
        print(f'Book "{title}" not found in library.')
        return False

    def return_book(self, title):
        """Return a book by title if it was checked out."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f'Book "{book.title}" has been returned.')
                    return True
                else:
                    print(f'Book "{book.title}" was not checked out.')
                    return False
        print(f'Book "{title}" not found in library.')
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f'  - "{book.title}" by {book.author}')
        else:
            print("No books available in the library right now.")
