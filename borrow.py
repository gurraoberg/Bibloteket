import sqlite3
from datetime import date, timedelta

library_db = "data/library.db"
lb = "\n" # Linebreak
today = date.today() # Todays date
connection = sqlite3.connect(library_db)
cursor = connection.cursor()

def table_register():
    cursor.execute("""CREATE TABLE IF NOT EXISTS book_register(
                TITLE TEXT,
                AUTHOR TEXT,
                PAGES TEXT,
                PRICE INT,
                YEAR INT,
                BORROWER TEXT,
                DAYS INT,
                DATE DATE
                )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS movie_register(
                TITLE TEXT,
                DIRECTOR TEXT,
                LENGTH INT,
                PRICE INT,
                YEAR INT,
                WEAR INT,
                BORROWER TEXT,
                DAYS INT,
                DATE DATE
                )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS cd_register(
                TITLE TEXT,
                ARTIST TEXT,
                TRACKS INT,
                LENGTH INT,
                PRICE INT,
                YEAR INT,
                BORROWER TEXT,
                DAYS INT,
                DATE DATE
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
        cursor.execute("SELECT * FROM library WHERE title=?", (title,))
        library = cursor.fetchone()
        cursor.execute("SELECT * FROM movies WHERE title=?", (title,))
        movies = cursor.fetchone()
        cursor.execute("SELECT * FROM cd WHERE title=?", (title,))
        cd = cursor.fetchone()
        
        print(f"Would you like to borrow {title}?")
        choice = input("Yes or No?: ").lower()
        if choice == "yes":
            duration = input("How many days would you like to borrow it?: ")
            name = input("What is your name: ")
            if library:
                cursor.execute("""INSERT INTO book_register (title,price,year,author,pages)
                            SELECT DISTINCT title,price,year,author,pages FROM library
                            WHERE library.title=?
                            """, (title,))
                connection.commit()
                cursor.execute("""UPDATE book_register SET borrower=?, days=?, date=? WHERE title=?
                            """,(name,duration,today,title,))
                connection.commit()
                cursor.execute("""DELETE FROM library
                            WHERE title=?
                            """, (title,))
                connection.commit()
            elif movies:
                cursor.execute("""INSERT INTO movie_register (title,director,length,price,year,wear)
                            SELECT title,director,length,price,year,wear FROM movies
                            WHERE title=?
                               """, (title,))
                connection.commit()
                cursor.execute("""UPDATE movie_register SET borrower=?, days=?, date=? WHERE title=?
                               """,(name,duration,today,title,))
                connection.commit()
                cursor.execute("""DELETE FROM movies
                            WHERE title=?
                            """, (title,))
                connection.commit()
            elif cd:
                cursor.execute("""INSERT INTO cd_register (title,artist,tracks,length,price,year)
                            SELECT title,artist,tracks,length,price,year FROM cd
                            WHERE title=?
                               """, (title,))
                connection.commit()
                cursor.execute("""UPDATE cd_register SET borrower=?, days=?, date=? WHERE title=?
                               """,(name,duration,today,title,))
                connection.commit()
                cursor.execute("""DELETE FROM cd
                            WHERE title=?
                            """, (title,))
                connection.commit()
            print(f"Succesfully borrowed {title} for {duration} days.")
        elif choice == "no":
            pass
        
def return_media():
    name = input(f"Return media{lb}Enter your name: ").lower()
    cursor.execute("""SELECT * FROM
                   (SELECT borrower FROM book_register
                   UNION ALL
                   SELECT borrower FROM movie_register
                   UNION ALL
                   SELECT borrower FROM cd_register
                   ) WHERE borrower=?
                   """, (name,))
    check = cursor.fetchone()
    
    if check == None:
        print(f"Sorry, {name} have not borrowed anything yet.")
    else:
        title = input("What title would you like to return?: ")
        cursor.execute("SELECT * FROM book_register WHERE title=?", (title,))
        library = cursor.fetchone()
        cursor.execute("SELECT * FROM movie_register WHERE title=?", (title,))
        movies = cursor.fetchone()
        cursor.execute("SELECT * FROM cd_register WHERE title=?", (title,))
        cd = cursor.fetchone()
        if title == None:
            print(f"Sorry, you never borrowed {title}.")
        else:
            if library:
                cursor.execute("""INSERT INTO library (title,price,year,author,pages)
                        SELECT title,price,year,author,pages FROM book_register
                        WHERE title=?
                        """, (title,))
                connection.commit()
                cursor.execute("""DELETE FROM book_register
                        WHERE title=?
                        """, (title,))
                connection.commit()
            elif movies:
                cursor.execute("""INSERT INTO movies (title,director,length,price,year,wear)
                            SELECT title,director,length,price,year,wear FROM movie_register
                            WHERE title=?
                            """, (title,))
                connection.commit()
                cursor.execute("""DELETE FROM movie_register
                            WHERE title=?
                            """, (title,))
                connection.commit()
            elif cd:
                cursor.execute("""INSERT INTO cd (title,artist,tracks,length,price,year)
                            SELECT title,artist,tracks,length,price,year FROM cd_register
                            WHERE title=?
                            """, (title,))
                connection.commit()
                cursor.execute("""DELETE FROM cd_register
                            WHERE title=?
                            """, (title,))
                connection.commit()
            print(f"Succesfully returned {title}.")
        
def who_borrowed():
    borrower = input("Search for borrower: ").lower()   
    cursor.execute("""SELECT * FROM
                   (SELECT title,days,date,borrower FROM book_register
                   UNION ALL
                   SELECT title,days,date,borrower FROM movie_register
                   UNION ALL
                   SELECT title,days,date,borrower FROM cd_register
                   ) WHERE borrower=?
                   """, (borrower,))
    check = cursor.fetchall()
    if check == None:
        print(f"Sorry, no one by that name has borrowed anything.")
    else:
        print(f"{lb}This person has borrowed.{lb}Name: {borrower}")
        for x in check:
            future_date = today + timedelta(days=x[1])
            print(f"Title: {x[0]} For {x[1]} days from {x[2]}.{lb}So it should be back by {future_date}.")