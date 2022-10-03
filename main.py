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
old_book_year = 1972

def menu(): # Menu
    print("1. Add Media")
    print("2. Search Media")
    print("3. Check Value")
    print("0. Exit")
    choice = input("Make a choice: ")
    if choice == "1":
        clear()
        print("1. Add Book")
        print("2. Add Movie")
        print("3. Add CD")
        print("0. Go back.")
        add_choice = input("Make a choice: ")
        if add_choice == "1":
            add_book()
            menu_back()
        elif add_choice == "2":
            pass
        elif add_choice == "3":
            pass
        elif add_choice == "0":
            clear()
            menu()
    elif choice == "2":
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
    elif choice == "3":
        clear()
        print("1. Check value of Media")
        print("2. Check value of the library.")
        print("0. Go back")
        value_choice = input("Make a choice: ")
        if value_choice == "1":
            book_value()
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
    
    with open(csv_media, "r") as file1, open(csv_movies) as file2, open(csv_cd) as file3:
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
                        YEAR INT)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS cd(
                        TITLE TEXT,
                        ARTIST TEXT,
                        TRACKS INT,
                        LENGTH INT,
                        PRICE INT)""")
        
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
                           ?,?,?,?,?)""", row)
            for row in data3:
                cursor.execute("""INSERT INTO cd
                           VALUES(
                           ?,?,?,?,?)""", row)
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
    
def add_book(): # Add book to library.
    connection = sqlite3.connect(library_db)
    cursor = connection.cursor()
    
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
        
    connection.commit()
    connection.close()

def clear(): # Clear the terminal
        os.system('cls' if os.name=='nt' else 'clear')

def book_value(): # FUNGERAR JÄLVIGT SVÅRT ATT LÖSA
    # Formeln är tex 100 / 0,9 = 90 osv... för att sänka värdet 10%
    connection = sqlite3.connect(library_db)
    cursor = connection.cursor()
    print("Check the values of a book.")
    title = input("Enter title: ")
    cursor.execute("SELECT * FROM library WHERE title=?", (title,))
    book = cursor.fetchone()
    if book == None:
        print("Book not found.")
    else:
        if book[4] < old_book_year:
            old_year = old_book_year - book[4]
            price_inc = book[3] * 1.08**(old_year) ## ÖKAR VÄRDET
            print(f"The book is very old so it has increased in value.{lb}The new price is {price_inc}sek.")
            return price_inc
        else:
            print(f"Purchase Price: {book[3]}sek{lb}Year: {book[4]}") # Hämtar priset på boken.
            new_int = current_year - book[4]
            new_price = book[3] * 0.9**(new_int) ### FUNKAR LÖST
            print(f"The book is {new_int} years old, so the current price is {new_price}sek.")
            return new_price
        
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
    value = cursor.fetchone()[0]
    if value == None:
        print("Error")
    else:
        print(f"Total value of the library is {value}sek.")
            

def main():
    import_library()
    menu()

if __name__ == "__main__":
    main()