import sqlite3
import json
import csv
import os
import classes

db_books = "data/books.db"
csv_books = "data/books.csv"

create_table_books = """
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Pages TEXT,
    Price TEXT,
    Year TEXT
)
"""
insert_books = """
INSERT INTO Books
VALUES (?, ?, ?, ?, ?)
"""



def import_database():
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    
    with open(csv_books, "r", encoding="utf-8") as file:
        bookdata = csv.reader(file)
        cursor.execute(create_table_books)
        
        for row in bookdata:
            cursor.execute(insert_books, row)     
            
    connection.commit()
    connection.close()
    
def search_database():
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    
    search = input("Search for book title: ").lower()
    cursor.execute("SELECT * FROM Books where title=?", (search,))
    title = cursor.fetchone()
    if title == None:
        print("Book not found.")
    else:
        print(title)
        
    connection.commit()
    connection.close()
    
def add_media():
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    
    title = input("Enter Title: ").lower()
    cursor.execute("SELECT * FROM Books WHERE title=?", (title,))
    add = cursor.fetchone()
    if add == None:
        author = input("Enter Author: ").lower()
        pages = input("Enter Pages: ").lower()
        price = input("Enter Price: ").lower()
        year = input("Enter Year: ").lower()
        cursor.execute("INSERT INTO Books VALUES (?, ?, ?, ?, ?)", (title, author, pages, price, year,))
        print(f"Added {title} to the library.")
    else:
        print("This book already exists.")
        
    connection.commit()
    connection.close()