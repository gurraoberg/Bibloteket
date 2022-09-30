import csv
import os
import classes
import sqlite3
import math

csv_path = "data/books.csv"
db_books = "data/books.db"
lb = "\n" # Linebreak
current_year = 2022
old_book_year = 1972

def menu():
    print("1. Add Media")
    print("2. Search Media")
    print("3. Check Value")
    print("0. Exit")
    choice = input("Make a choice: ")
    if choice == "1":
        clear()
        print("1. Add Book")
        print("2. Add Movie / Check lib value")
        print("3. Add CD")
        print("0. Go back.")
        add_choice = input("Make a choice: ")
        if add_choice == "1":
            add_book()
        elif add_choice == "2":
            whole_value()
        elif add_choice == "3":
            pass
        elif add_choice == "0":
            clear()
            menu()
    elif choice == "2":
        clear()
        print("1. Search books")
        print("2. List books")
        print("0. Go back.")
        search_choice = input("Make a choice: ")
        if search_choice == "1":
            search_books()
        elif search_choice == "2":
            sorted_book()
        elif search_choice == "0":
            clear()
            menu()
    elif choice == "3":
        book_value()
    elif choice == "0":
        exit()

def import_books():
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    
    with open(csv_path, "r", encoding = "utf-8") as file:
        bookdata = csv.reader(file)
        cursor.execute("""CREATE TABLE IF NOT EXISTS books(
                       Title TEXT,
                       Author TEXT,
                       Pages TEXT,
                       Price INT,
                       Year INT)""")
        if db_books is None: # Doesnt work, prints duplicates. FIX LATER
            pass
        else:
            for row in bookdata:
                cursor.execute("""INSERT INTO books
                           VALUES(
                           ?,?,?,?,?)""", row)
            
        connection.commit()
        connection.close()

def search_books():
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    
    search = input("Search for book title: ").lower()
    cursor.execute("SELECT * FROM books WHERE Title=?", (search,))
    book = cursor.fetchone()
    if book == None:
        print("Book not found.")
        menu()
    else:
        print(f"Title: {book[0]}{lb}Author: {book[1]}{lb}Pages: {book[2]}{lb}Purchase price: {book[3]}{lb}Publishing year: {book[4]}")
        print(f"Current value: ")
        back = input("\nGo back to menu, Enter 0: ")
        if back == "0":
            menu()
        else:
            print("Press 0 to go back to menu.")
    
def add_book():
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
        menu()
        
    connection.commit()
    connection.close()

def clear(): # Clear the terminal
        os.system('cls' if os.name=='nt' else 'clear')

def book_value(): # FUNGERAR JÄLVIGT SVÅRT ATT LÖSA
    # Formeln är tex 100 / 0,9 = 90 osv... för att sänka värdet 10%
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    print("Check the values of a book.")
    title = input("Enter title: ")
    cursor.execute("SELECT * FROM books WHERE title=?", (title,))
    book = cursor.fetchone()
    if book == None:
        print("Book not found.")
    else:
        if book[4] < old_book_year:
            old_year = old_book_year - book[4]
            price_inc = book[3] * 1.08**(old_year) ## ÖKAR VÄRDET
            print(f"The book is very old so it has increased in value.{lb}The new price is {price_inc}sek.")
        else:
            print(f"Purchase Price: {book[3]}sek{lb}Year: {book[4]}") # Hämtar priset på boken.
            new_int = current_year - book[4]
            new_price = book[3] * 0.9**(new_int) ### FUNKAR LÖST
            print(f"The book is {new_int} years old, so the current price is {new_price}sek.")

def sorted_book():
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM books ORDER BY title")
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

def whole_value():
    connection = sqlite3.connect(db_books)
    cursor = connection.cursor()
    
    cursor.execute("SELECT SUM(price) FROM books") ## Fungerar, behöver snyggas till.
    value = cursor.fetchall()
    if value == None:
        print("Error")
    else:
        print(value)
            

def main():
    import_books()
    menu()

if __name__ == "__main__":
    main()