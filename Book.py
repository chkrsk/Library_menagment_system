import sqlite3

class Book:

    def __init__(
            self, title: str, author: str, publisher: str, 
            year_of_production: int):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year_of_production = year_of_production


class Reader:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.points = 0