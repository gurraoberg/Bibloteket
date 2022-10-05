import os
import sqlite3

library_db = "data/library.db"
lb = "\n" # Linebreak
connection = sqlite3.connect(library_db)
cursor = connection.cursor()

def table_register():
    #cursor.execute("DROP TABLE IF EXISTS book_register,movie_register,cd_register")
    cursor.execute("""CREATE TABLE IF NOT EXISTS book_register(
                TITLE TEXT,
                AUTHOR TEXT,
                PAGES TEXT,
                PRICE INT,
                YEAR INT,
                BORROWER TEXT,
                DAYS INT
                )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS movie_register(
                TITLE TEXT,
                DIRECTOR TEXT,
                LENGTH INT,
                PRICE INT,
                YEAR INT,
                WEAR INT,
                BORROWER TEXT,
                DAYS INT
                )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS cd_register(
                TITLE TEXT,
                ARTIST TEXT,
                TRACKS INT,
                LENGTH INT,
                PRICE INT,
                YEAR INT,
                BORROWER TEXT,
                DAYS INT
                )""")

def borrow():
    title = input("Search for title: ").lower()
    cursor.execute("""SELECT * FROM
                   (SELECT title FROM library
                   UNION ALL
                   SELECT title FROM movies
                   UNION ALL
                   SELECT title FROM cd
                   ) WHERE title=?
                   """, (title,))
    check = cursor.fetchone()
    if check == None:
        print(f"{title} doesn't exist in our library.")
    else:
        print(f"Would you like to borrow {title}?")
        choice = input("Yes or No?: ").lower()
        if choice == "yes":
            duration = input("How many days would you like to borrow it?: ")
            name = input("What is your name: ")
            cursor.execute("""INSERT INTO book_register (title,price,year,author,pages)
                           SELECT title,price,year,author,pages FROM library
                           WHERE title=? 
                           """, (title,))
            connection.commit()
            cursor.execute("""UPDATE book_register SET borrower=?, days=? WHERE title=?
                           """,(name,duration,title,))
            connection.commit()
            cursor.execute("""DELETE FROM library
                           WHERE title=?
                           """, (title,))
            connection.commit()
            print(f"Succesfully borrowed {title} for {duration} days.")
        elif choice == "no":
            pass
        
def return_media():
    media = input(f"Whats the title of the media you want to return?{lb}Enter Title: ").lower()
    cursor.execute("SELECT * FROM book_register WHERE title=?",(media,))
    check_register = cursor.fetchone()
    if check_register == None:
        print(f"Sorry, {media} doesn't seem to be borrowed.")
    else:
        cursor.execute("""INSERT INTO library (title,price,year,author,pages)
                       SELECT title,price,year,author,pages FROM book_register
                       WHERE title=?
                       """, (media,))
        connection.commit()
        cursor.execute("""DELETE FROM book_register
                       WHERE title=?
                       """, (media,))
        connection.commit()
        print(f"Succesfully returned {media}.")