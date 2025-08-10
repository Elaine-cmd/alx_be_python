"""
This module defines a system for a library, including classes for
Book, EBook, PrintBook, and Library.
"""

class Book:
    """
    A base class representing a generic book.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title, author):
        """Initializes the Book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation for a generic book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    A class representing an electronic book, inheriting from Book.

    Attributes:
        file_size (int): The file size of the ebook in KB.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes the EBook, calling the parent constructor.

        Args:
            file_size (int): The file size of the ebook.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation for an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    A class representing a physical book, inheriting from Book.

    Attributes:
        page_count (int): The number of pages in the book.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes the PrintBook, calling the parent constructor.

        Args:
            page_count (int): The number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation for a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class representing a library, which contains a collection of books.
    This class demonstrates composition.
    """
    def __init__(self):
        """Initializes the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """
        Adds a book instance to the library's collection.

        Args:
            book (Book): An instance of Book or its subclasses.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        """
        for book in self.books:
            print(book)