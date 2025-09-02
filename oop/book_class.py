# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation (re-creatable form)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
