import csv
import os
import classes
import sqlite3
import math

csv_media = "data/media.csv"
csv_movies = "data/movies.csv"
csv_cd = "data/cd.csv"
library_db = "data/library.db"
lb = "\n" # Linebreak
current_year = 2022
year_inc = 1972

def menu(): # Menu
    print("1. Add Media")
    print("2. Search Media")
    print("3. Check Value")
    print("0. Exit")
    choice = input("Make a choice: ")
    if choice == "1": # Add
        clear()
        add_media()
        menu_back()
    elif choice == "2": # Search
        clear()
        print("1. Search books")
        print("2. List books in ascending order")
        print("0. Go back.")
        search_choice = input("Make a choice: ")
        if search_choice == "1":
            search_books()
            menu_back()
        elif search_choice == "2":
            sorted_book()
            menu_back()
        elif search_choice == "0":
            clear()
            menu()
    elif choice == "3": # Value
        clear()
        print("1. Check value of Media")
        print("2. Check value of the library.")
        print("0. Go back")
        value_choice = input("Make a choice: ")
        if value_choice == "1":
            check_value()
            menu_back()
        elif value_choice == "2":
            whole_value()
            menu_back()
        elif value_choice == "0":
            clear()
            menu()
    elif choice == "0":
        exit()

def menu_back(): # Goes back to menu.
        back = input("\nGo back to menu, Enter 0: ")
        if back == "0":
            clear()
            menu()
        else:
            print("Press 0 to go back to menu.")

def import_library(): # Creating SQL table and importing CSV to it.
    connection = sqlite3.connect(library_db)
    cursor = connection.cursor()
    
    with open(csv_media, "r", encoding="utf-8") as file1, open(csv_movies) as file2, open(csv_cd) as file3:
        data1 = csv.reader(file1)
        data2 = csv.reader(file2)
        data3 = csv.reader(file3)
        cursor.execute("""CREATE TABLE IF NOT EXISTS library(
                       TITLE TEXT,
                       AUTHOR TEXT,
                       PAGES TEXT,
                       PRICE INT,
                       YEAR INT)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS movies(
                        TITLE TEXT,
                        DIRECTOR TEXT,
                        LENGTH INT,
                        PRICE INT,
                        YEAR INT,
                        WEAR INT)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS cd(
                        TITLE TEXT,
                        ARTIST TEXT,
                        TRACKS INT,
                        LENGTH INT,
                        PRICE INT,
                        YEAR INT)""")
        
        cursor.execute("SELECT COUNT(*) FROM library") 
        check_empty = cursor.fetchall()
        if check_empty[0][0] == 0: # Check if table is empty, if empty insert CSV.
            print("Table is empty.") # Avoiding duplicates at the start.
            for row in data1:
                cursor.execute("""INSERT INTO library
                           VALUES(
                           ?,?,?,?,?)""", row)
            for row in data2:
                cursor.execute("""INSERT INTO movies
                           VALUES(
                           ?,?,?,?,?,?)""", row)
            for row in data3:
                cursor.execute("""INSERT INTO cd
                           VALUES(
                           ?,?,?,?,?,?)""", row)
            print("Inserting values")
        else:
            print("Table not empty")
            
        connection.commit()
        connection.close()

def search_books(): # Search for a book with title.
    connection = sqlite3.connect(library_db)
    cursor = connection.cursor()
    
    search = input("Search for book title: ").lower()
    cursor.execute("SELECT * FROM library WHERE Title=?", (search,))
    book = cursor.fetchone()
    if book == None:
        print("Book not found.")
        menu()
    else:
        print(f"Title: {book[0]}{lb}Author: {book[1]}{lb}Pages: {book[2]}{lb}Purchase price: {book[3]}{lb}Publishing year: {book[4]}")
        #print(f"Current value: {new_price}")
    
def add_media(): # Add media to library.
    connection = sqlite3.connect(library_db)
    cursor = connection.cursor()
    
    print("1. Add book")
    print("2. Add movie")
    print("3. Add CD")
    choice = input("Make a choice: ")
    if choice == "1": # Add book
        title = input("Enter Title: ").lower()
        cursor.execute("SELECT * FROM library WHERE title=?", (title,))
        add = cursor.fetchone()
        if add == None:
            author = input("Enter Author: ").lower()
            pages = input("Enter Pages: ").lower()
            price = input("Enter Price: ").lower()
            year = input("Enter Year: ").lower()
            cursor.execute("INSERT INTO library VALUES (?, ?, ?, ?, ?)", (title, author, pages, price, year,))
            print(f"Added {title} to the library.")
        else:
            print("This book already exists.")
            menu()
    elif choice == "2": # Add movie
        title = input("Enter Title: ").lower()
        cursor.execute("SELECT * FROM movies WHERE title=?", (title,))
        add = cursor.fetchone()
        if add == None:
            director = input("Enter Director: ").lower()
            length = input("Enter Movie Length: ").lower()
            price = input("Enter Price: ").lower()
            year = input("Enter Year: ").lower()
            wear = input("Enter Wear: ")
            cursor.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?)", (title, director, length, price, year, wear,))
            print(f"Added {title} to the movie library.")
        else:
            print("This movie already exists.")
            menu()
    elif choice == "3": # Add CD
        title = input("Enter Title: ").lower()
        cursor.execute("SELECT * FROM cd WHERE title=?", (title,))
        add = cursor.fetchone()
        if add == None:
            artist = input("Enter Artist: ").lower()
            tracks = input("Enter amount of Tracks: ").lower()
            length = input("Enter length: ").lower()
            price = input("Enter Price: ").lower()
            year = input("Enter Year: ").lower()
            cursor.execute("INSERT INTO cd VALUES (?, ?, ?, ?, ?, ?)", (title, artist, tracks, length, price, year,))
            print(f"Added {title} to the CD library.")
        else:
            print("This CD already exists, would you like to add it anyway? ")
            choice = input("Yes or No: ").lower()
            if choice == "yes":
                print(f"Title: {title}")
                artist = input("Enter Artist: ").lower()
                tracks = input("Enter amount of Tracks: ").lower()
                length = input("Enter length: ").lower()
                price = input("Enter Price: ").lower()
                year = input("Enter Year: ").lower()
                cursor.execute("INSERT INTO cd VALUES (?, ?, ?, ?, ?, ?)", (title, artist, tracks, length, price, year,))
                print(f"Added {title} to the CD library.")
            else:
                menu()
            
    connection.commit()
    connection.close()

def clear(): # Clear the terminal
        os.system('cls' if os.name=='nt' else 'clear')

def check_value(): # FUNGERAR JÄLVIGT SVÅRT ATT LÖSA 
    # Formeln är tex 100 / 0,9 = 90 osv... för att sänka värdet 10%
    connection = sqlite3.connect(library_db)
    cursor = connection.cursor()
    
    print("1. Check value of a book")
    print("2. Check value of a movie")
    print("3. Check value of a CD")
    print("0. Go back.")
    choice = input("Make a choice: ")
    
    if choice == "1": # Check value of a book
        print("Check the values of a book.")
        title = input("Enter title: ")
        cursor.execute("SELECT * FROM library WHERE title=?", (title,))
        book = cursor.fetchone()
        if book == None:
            print("Book not found.")
        else:
            if book[4] < year_inc:
                old_year = year_inc - book[4]
                price_inc = book[3] * 1.08**(old_year) ## ÖKAR VÄRDET
                print(f"The book is very old so it has increased in value.{lb}The new price is {price_inc:.2f}sek.")
            else:
                print(f"Purchase Price: {book[3]}sek{lb}Year: {book[4]}") # Hämtar priset på boken.
                new_int = current_year - book[4]
                new_price = book[3] * 0.9**(new_int) ### FUNKAR LÖST
                print(f"The book is {new_int} years old, so the current price is {new_price:.2f}sek.")
    elif choice == "2": # Check value of a movie
        print("Check the values of a movie.")
        title = input("Enter title: ")
        cursor.execute("SELECT * FROM movies WHERE title=?", (title,))
        movie = cursor.fetchone()
        if movie == None:
            print("Movie not found.")
        else:
            if movie[4] < year_inc:
                pass #
            else:
                print(f"Purchase Price: {movie[3]}sek{lb}Year: {movie[4]}")
                new_int = current_year - movie[4]
                new_price = movie[3] * 0.9**(new_int)
                print(f"The movie is {new_int} years old, so the current price is {new_price:.2f}sek.")
    elif choice == "3": # Check value of a CD # Doesnt work yet
        print("Check the values of a CD.")
        title = input("Enter album title: ")
        cursor.execute("SELECT * FROM cd WHERE title=?", (title,))
        cd = cursor.fetchone()
        cursor.execute("SELECT COUNT(title) FROM cd GROUP BY title HAVING COUNT(title) > 1")
        multiple = cursor.fetchmany(2)
        for x in multiple:
            value = int(x[0])
        
        if cd == None:
            print("CD not found.")
        else:
            if value > 1:
                        result = cd[4] / value
                        print(f"{title} is worth {result:.0f}sek, since we have {value} copies of it.")

    elif choice == "0":
        menu()
        
def sorted_book(): # Sorted books in ascending order.
    connection = sqlite3.connect(library_db)
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM library ORDER BY title")
    result = cursor.fetchall()
    if result == None:
        print("Book not found.")
        menu()
    else:
        print(f"Sorted by title: {result[0]}{lb}") # Sorted by ascending order.
        back = input("\nGo back to menu, Enter 0: ")
        if back == "0":
            menu()
        else:
            print("Press 0 to go back to menu.")
            
    connection.commit()
    connection.close()

def whole_value(): # Prints the combined value of the library.
    connection = sqlite3.connect(library_db)
    cursor = connection.cursor()
    
    cursor.execute("SELECT SUM(price) FROM library") ## Fungerar
    books = cursor.fetchone()[0]
    cursor.execute("SELECT SUM(price) FROM movies")
    movies = cursor.fetchone()[0]
    cursor.execute("SELECT SUM(price) FROM cd")
    cd = cursor.fetchone()[0]
    value = books + movies + cd
    if value == None:
        print("Error")
    else:
        print(f"Total value of the library is {value:.2f}sek.")
            

def main():
    import_library()
    menu()

if __name__ == "__main__":
    main()