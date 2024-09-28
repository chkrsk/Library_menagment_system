import sqlite3
from typing import List


class Book:

    def __init__(
            self, id: int, title: str, author: str, publisher: str,
            year_of_production: int, status: bool = True) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year_of_production = year_of_production
        # True - (avaliable) can borrow | False (not avaliable) can't borrow
        self.status = status

    @property
    def status(self):
        """The status property."""
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


class Reader:

    def __init__(self, name: str, surname: str, limit: int = 2) -> None:
        self.name = name
        self.surname = surname
        self.points = 0
        # Determines how many books can be borrowed at one time
        self.limit = limit
        self.borrowed_books: List[Book] = []

    def add_point(self) -> None:
        """method to add a point for the user"""
        self.points += 1

    def borow_the_books(self, book: Book):
        """method for serving readers when borrowing books."""
        if len(self.borrowed_books) < self.limit and book.status:
            self.borrowed_books.append(book)
            self.add_point()
            book.status = False
        else:
            if len(self.borrowed_books) == self.limit:
                print("You can't boorow the book because"
                      f"you have {self.limit} books")
            else:
                print("This book isn't available")
