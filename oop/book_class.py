"""
This module defines the Book class.
"""

class Book:
    """
    A class to represent a book, demonstrating magic methods.
    """

    def __init__(self, title, author, year):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Prints a message upon object deletion.
        This is the destructor method.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns an informal, user-friendly string representation of the book.

        Returns:
            str: A string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official, developer-friendly string representation of the book
        that can be used to recreate the instance.

        Returns:
            str: A string in the format "Book('title', 'author', year)".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
