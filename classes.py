import json
import os
import sqlite3

library_db = "data/library.db"
current_year = 2022
year_inc = 1972

class Book:
    def __init__(self) -> None:
        pass
    def current_price(self):
        connection = sqlite3.connect(library_db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM library WHERE title")
        book = cursor.fetchone()
        new_int = current_year - book[4]
        new_price = book[3] * 0.9**(new_int)
        return new_price
        
class Movie:
    def __init__(self, title, director, playtime, price, year) -> None:
        self.title = title
        self.director = director
        self.playtime = playtime
        self.price = price
        self.year = year
    
    def __str__(self) -> str:
        return f"Title: {self.title} Director: {self.director} Playtime: {self.playtime} Price: {self.price}sek Year: {self.year}"
        
class CD:
     
    def __init__(self, title, artist, tracks, playtime, price) -> None:
        self.title = title
        self.artist = artist
        self.tracks = tracks
        self.playtime = playtime
        self.price = price
        
